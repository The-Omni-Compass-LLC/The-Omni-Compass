# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Conservative CPU-limit admission budget; Kubernetes remains the final authority."""
from decimal import Decimal, InvalidOperation
import re


def cpu_milli(value):
    match = re.fullmatch(r'([+\-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+\-]?\d+)?)([numkMGTPE]?)', str(value))
    if not match:
        raise ValueError('invalid CPU quantity')
    factor = {'n': '0.000001', 'u': '0.001', 'm': '1', '': '1000', 'k': '1000000',
              'M': '1e9', 'G': '1e12', 'T': '1e15', 'P': '1e18', 'E': '1e21'}
    result = Decimal(match[1]) * Decimal(factor[match[2]])
    if not result.is_finite() or result < 0:
        raise ValueError('invalid CPU quantity')
    return result


def matches(quota, pod):
    """True/False for PriorityClass selectors; None means applicability is unknown, so expansion stops."""
    spec = quota.get('spec', {})
    if spec.get('scopes'):
        return None
    expressions = spec.get('scopeSelector', {}).get('matchExpressions', [])
    unknown = False
    for expr in expressions:
        if expr.get('scopeName') != 'PriorityClass':
            unknown = True
            continue
        value = pod.get('spec', {}).get('priorityClassName', '')
        operator, values = expr.get('operator'), expr.get('values', [])
        if operator == 'In':
            selected = value in values
        elif operator == 'NotIn':
            selected = value not in values
        elif operator == 'Exists':
            selected = bool(value)
        elif operator == 'DoesNotExist':
            selected = not value
        else:
            unknown = True
            continue
        if not selected:
            return False
    return None if unknown else True


class CpuLimitBudget:
    """One convey pass: share each namespace's headroom across all target deployments.

    Never credit a decrease before the server reports it. Reserve successful increases locally
    so an eventually updated quota status cannot spend the same allowance twice in this pass.
    A quota whose status or scopes cannot be read as a number leaves the native CPU limit in place.

    A namespace whose quotas cannot be read at all (the governor's role has no list permission, or the API refused) is
    **no budget known**, not a zero budget: the raise proceeds as it did before the budget existed (omni-v6), and
    Kubernetes' own admission, which refuses any write over a quota the governor cannot see, stays the authority; the
    plug reads every write back and a refused one is audited and never advertised. The first v7 trial (Goldilocks, run
    38825214203) read the unreadable quota as zero and so never raised a limit: 5 commands a run against v6's 15, the
    host 4% busier against 40%, the response-time GAIN gone and the pod start wait a LOSS (docs/OMNI_V7.md, section 1).
    """
    def __init__(self, kube, audit):
        self.kube, self.audit, self.namespaces, self.unreadable = kube, audit, {}, set()

    def _load(self, namespace):
        if namespace in self.namespaces:
            return self.namespaces[namespace]
        try:
            quotas = self.kube.get('get', 'resourcequota', '-n', namespace, '-o', 'json')['items']
            budgets = []
            for quota in quotas:
                spec = quota.get('spec', {}).get('hard', {})
                status = quota.get('status', {})
                hard = status.get('hard', {})
                if 'limits.cpu' not in spec and 'limits.cpu' not in hard:
                    continue
                try:
                    ceiling = min(cpu_milli(x['limits.cpu']) for x in (spec, hard))
                    remaining = max(Decimal(0), ceiling - cpu_milli(status['used']['limits.cpu']))
                except (KeyError, ValueError, InvalidOperation):
                    remaining = Decimal(0)
                budgets.append([quota, remaining])
        except Exception as error:
            if namespace not in self.unreadable:                    # said once a pass, not once a pod
                self.audit({'quota': 'no budget known: the raise proceeds, Kubernetes admission is the authority',
                            'namespace': namespace, 'reason': f'quota read unavailable: {type(error).__name__}'})
            self.unreadable.add(namespace)
            budgets = []
        self.namespaces[namespace] = budgets
        return budgets

    def limit(self, namespace, pod, current, desired):
        current, desired = Decimal(str(current)), Decimal(str(desired))
        if desired <= current:
            return int(desired), []
        budgets = self._load(namespace)
        applicable = []
        allowance = desired - current
        for entry in budgets:                       # an unreadable namespace has no entries: the allowance stands
            selected = matches(entry[0], pod)
            if selected is False:
                continue
            applicable.append(entry)
            allowance = min(allowance, entry[1] if selected is True else Decimal(0))
        permitted = int(current + allowance)
        if permitted < desired:
            self.audit({'quota': 'CPU limit expansion bounded', 'namespace': namespace,
                        'pod': pod['metadata']['name'], 'desired_m': int(desired), 'permitted_m': permitted})
        return permitted, applicable

    @staticmethod
    def reserve(entries, current, accepted):
        delta = max(Decimal(0), Decimal(str(accepted)) - Decimal(str(current)))
        for entry in entries:
            entry[1] = max(Decimal(0), entry[1] - delta)
