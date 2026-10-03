from pathlib import Path
import importlib.util

def load_mod():
    p=Path(__file__).parents[1]/'tournament'/'xpass15_allocator_holdout.py'
    spec=importlib.util.spec_from_file_location('x15',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def test_xpass15_policy_is_explicit_and_core_unchanged_by_runner():
    m=load_mod()
    src=(Path(m.__file__)).read_text()
    assert 'sizer=RequestSizer() if arm==\'hpa70_karpenter_vpa\' else None' in src
    assert 'OmniFleetLaw(cap_min=0.45, cap_margin=0.02)' in src
    assert m.ARMS['C7_OMNI_COMPASS_CLAIM1']=='omni_full'

def test_control_effort_penalizes_motion():
    m=load_mod(); r={k:0.0 for k in ['replica_change_units','evictions','node_starts','node_stops','request_changes','replica_reversals','power_cap_travel']}
    base=m.ce(r,m.DEFAULT_CE); r['node_starts']=1
    assert m.ce(r,m.DEFAULT_CE)>base
