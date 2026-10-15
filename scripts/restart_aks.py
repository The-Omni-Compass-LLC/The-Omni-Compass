#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Apply one explicitly requested AKS stop/cleanup/restart; never cancel unrelated runs."""
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def gh_api(path, method='GET', body=None):
    cmd = ['gh', 'api', path, '--method', method]
    if body is not None:
        cmd += ['--input', '-']
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None,
                       text=True, capture_output=True, check=True)
    return json.loads(r.stdout) if r.stdout.strip() else None


def main(argv=None):
    request = json.loads(Path((argv or sys.argv[1:])[0]).read_text())
    repo = os.environ['GITHUB_REPOSITORY']
    base = f'repos/{repo}'
    receipt = {'request': request, 'cancelled': [], 'resource_groups_deleted': [], 'restart': None}
    out = Path('aks-restart-receipt.json')
    def save():
        out.write_text(json.dumps(receipt, indent=2) + '\n')
    save()
    # Cancel the obsolete pending run before freeing the active run's queue slot.
    for old in request['superseded_runs']:
        run = gh_api(f'{base}/actions/runs/{old["id"]}')
        if run['path'] != '.github/workflows/' + old['workflow'] or run['head_branch'] != 'main':
            raise RuntimeError('run identity did not match the explicit restart request')
        if run['status'] != 'completed':
            try:
                gh_api(f'{base}/actions/runs/{old["id"]}/cancel', 'POST')
            except subprocess.CalledProcessError:
                if gh_api(f'{base}/actions/runs/{old["id"]}')['status'] != 'completed':
                    raise
        receipt['cancelled'].append({'id': old['id'], 'previous_status': run['status']})
        save()
    # Give each cancelled job its normal always() cleanup before issuing the same bounded cleanup ourselves.
    deadline = time.monotonic() + 360
    while time.monotonic() < deadline:
        states = [gh_api(f'{base}/actions/runs/{x["id"]}')['status'] for x in request['superseded_runs']]
        if all(s == 'completed' for s in states):
            break
        time.sleep(10)
    else:
        raise RuntimeError('the cancelled runs have not finished cleanup; the new test was not started')
    groups = []
    for old in request['superseded_runs']:
        if old['workflow'] not in ('aks-metered.yml', 'aks-metered-full.yml'):
            raise ValueError('restart supports only the two named AKS benchmark workflows')
        prefix = 'omni-compass-bench-' if old['workflow'] == 'aks-metered.yml' else 'omni-compass-full-'
        for rep in range(1, old['reps'] + 1):
            group = f'{prefix}{old["id"]}-{rep}'
            exists = subprocess.check_output(['az', 'group', 'exists', '-n', group], text=True).strip()
            if exists == 'true':
                subprocess.run(['az', 'group', 'delete', '-n', group, '--yes', '--no-wait'], check=True)
                groups.append(group)
    deadline = time.monotonic() + 900
    while groups and time.monotonic() < deadline:
        groups = [g for g in groups if subprocess.check_output(['az', 'group', 'exists', '-n', g], text=True).strip() == 'true']
        if groups:
            print('Waiting for the old billed resources to be deleted:', ', '.join(groups), flush=True)
            time.sleep(15)
    if groups:
        raise RuntimeError('Azure is still deleting the old resources; refusing a competing billed test')
    receipt['resource_groups_deleted'] = True
    save()
    started = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    gh_api(f'{base}/actions/workflows/aks-metered-full.yml/dispatches', 'POST',
           {'ref': 'main', 'inputs': request['inputs']})
    receipt['restart'] = {'dispatch_accepted': True, 'inputs': request['inputs']}
    for _ in range(12):
        d = gh_api(f'{base}/actions/workflows/aks-metered-full.yml/runs?event=workflow_dispatch&per_page=10')
        matches = [r for r in d['workflow_runs'] if dt.datetime.fromisoformat(r['created_at'].replace('Z', '+00:00')) >= started
                   and r['head_branch'] == 'main']
        if matches:
            r = max(matches, key=lambda x: x['id'])
            receipt['restart'].update({'id': r['id'], 'url': r['html_url'], 'status': r['status']})
            break
        time.sleep(3)
    save()
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a') as f:
            f.write('\nSuperseded runs cancelled and their resource groups removed.\n\n')
            f.write('Replacement Azure run: ' + json.dumps(receipt['restart']) + '\n')
    print(json.dumps(receipt['restart']), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
