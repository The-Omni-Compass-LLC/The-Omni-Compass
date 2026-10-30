#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Collect continuous pod events and reconcile benchmark-owned rollout cleanup."""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path
import subprocess
import time
from urllib.parse import urlencode

PAUSE = 'omnicompass.io/paused-by-omni'


def read_events(text):
    decoder = json.JSONDecoder()
    while text.strip():
        event, end = decoder.raw_decode(text.lstrip())
        if event.get('type') == 'ERROR':
            raise ValueError('pod watch API error: ' + str(event.get('object')))
        yield event
        text = text.lstrip()[end:]


def collect(directory, kubectl='kubectl', run=subprocess.run, popen=subprocess.Popen):
    """A LIST followed by watches at its resourceVersion; never relist across a gap.

    Every clean server timeout resumes the last event/bookmark's resourceVersion.
    Expired history, malformed JSON and nonzero client exits fail the receipt.
    A stop file drains the current bounded request before the collector exits.
    """
    directory = Path(directory)
    receipt = {'schema': 1, 'complete': False, 'started_at': time.time(), 'segments': 0}
    stop = directory / 'pod_watch.stop'
    for name in ('pod_watch.ready', 'pod_watch_receipt.json'):
        (directory / name).unlink(missing_ok=True)
    try:
        result = run([kubectl, 'get', 'pods', '-n', 'default', '-l', 'run=php-apache',
                      '-o', 'json', '--request-timeout=20s'], check=True, capture_output=True, text=True)
        listing = json.loads(result.stdout)
        version = listing['metadata']['resourceVersion']
        with (directory / 'pod_watch.json').open('w') as output:
            for pod in listing['items']:
                output.write(json.dumps({'type': 'ADDED', 'object': pod}) + '\n')
            output.flush()
            (directory / 'pod_watch.ready').touch()
            with (directory / 'pod_watch.err').open('w') as errors:
                while not stop.exists():
                    query = urlencode({'watch': 'true', 'labelSelector': 'run=php-apache',
                                       'resourceVersion': version, 'allowWatchBookmarks': 'true',
                                       'timeoutSeconds': 30})
                    process = popen([kubectl, 'get', '--raw', '/api/v1/namespaces/default/pods?' + query,
                                     '--request-timeout=40s'], stdout=subprocess.PIPE, stderr=errors, text=True)
                    try:
                        for line in process.stdout:
                            if not line.strip():
                                continue
                            for event in read_events(line):
                                version = event['object']['metadata']['resourceVersion']
                                output.write(json.dumps(event) + '\n')
                                output.flush()
                        if process.wait() != 0:
                            raise RuntimeError('pod watch client failed; see pod_watch.err')
                    finally:
                        process.stdout.close()
                        if process.poll() is None:
                            process.terminate()
                            process.wait(timeout=5)
                    receipt['segments'] += 1
                    receipt['last_resource_version'] = version
        receipt['complete'] = True
    except Exception as error:
        receipt['error'] = str(error)
        raise
    finally:
        receipt['ended_at'] = time.time()
        (directory / 'pod_watch_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')


def validate(directory):
    directory = Path(directory)
    receipt = json.loads((directory / 'pod_watch_receipt.json').read_text())
    start = float((directory / 'window_start.txt').read_text())
    end = float((directory / 'window_end.txt').read_text())
    if not receipt.get('complete') or not receipt.get('segments'):
        raise ValueError('pod watch did not complete: ' + str(receipt.get('error', 'no segment')))
    if int(receipt['started_at']) > start or receipt['ended_at'] < end or end < start:
        raise ValueError('pod watch does not cover the measured window')
    observed = {}
    for event in read_events((directory / 'pod_watch.json').read_text()):
        pod = event.get('object', event)
        uid = pod.get('metadata', {}).get('uid')
        if uid:
            transitions = observed.setdefault(uid, set())
            for condition in (pod.get('status') or {}).get('conditions', []) or []:
                if condition.get('status') == 'True':
                    transitions.add((condition.get('type'), condition.get('lastTransitionTime')))
    final = json.loads((directory / 'pods_end.json').read_text())
    for pod in final['items']:
        uid = pod['metadata']['uid']
        created = dt.datetime.fromisoformat(pod['metadata']['creationTimestamp'].replace('Z', '+00:00')).timestamp()
        if created > end:
            continue
        if uid not in observed:
            raise ValueError('pod missing from watch: ' + uid)
        for condition in (pod.get('status') or {}).get('conditions', []) or []:
            stamp = condition.get('lastTransitionTime')
            if condition.get('type') not in ('Ready', 'PodScheduled') or condition.get('status') != 'True' or not stamp:
                continue
            when = dt.datetime.fromisoformat(stamp.replace('Z', '+00:00')).timestamp()
            if when <= end and (condition['type'], stamp) not in observed[uid]:
                raise ValueError('pod watch missed ' + condition['type'] + ' transition: ' + uid)
    return receipt


def restore_rollout(target, kubectl='kubectl', run=subprocess.run):
    """Reset only the rollout this benchmark owns; one atomic, idempotent patch.

    A resourceVersion precondition rejects concurrent changes. An API/permission
    error propagates, and the reread must confirm both unpaused and unannotated.
    """
    namespace, name = target.split('/', 1)
    def get():
        return json.loads(run([kubectl, 'get', 'deployment', name, '-n', namespace, '-o', 'json',
                               '--request-timeout=20s'], check=True, capture_output=True, text=True).stdout)
    deployment = get()
    if (deployment['metadata'].get('annotations') or {}).get(PAUSE) != 'true':
        return False
    patch = {'metadata': {'resourceVersion': deployment['metadata']['resourceVersion'],
                          'annotations': {PAUSE: None}}, 'spec': {'paused': False}}
    run([kubectl, 'patch', 'deployment', name, '-n', namespace, '--type=merge', '-p', json.dumps(patch),
         '--request-timeout=20s'], check=True, capture_output=True, text=True)
    restored = get()
    if restored['spec'].get('paused') or PAUSE in (restored['metadata'].get('annotations') or {}):
        raise ValueError('rollout reset did not restore the deployment')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('collect', 'validate', 'restore-rollout'))
    parser.add_argument('target')
    parser.add_argument('--kubectl', default='kubectl')
    args = parser.parse_args()
    if args.action == 'collect':
        collect(args.target, args.kubectl)
    elif args.action == 'validate':
        print(json.dumps(validate(args.target)))
    else:
        print(json.dumps({'rollout_reset': restore_rollout(args.target, args.kubectl)}))


if __name__ == '__main__':
    main()
