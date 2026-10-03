from organism.xpass21_organism_lab import catalog,run,BREADTH,ARMS

def test_catalog(): assert len(catalog())==640
def test_arms(): assert ARMS==('NATIVE','OMNI_OVER_NATIVE')
def test_each_breadth_is_simultaneous():
    for m in BREADTH:
        rows=run(3,m,2,17,chunk=2)
        for r in rows:
            assert r['breadth']==m and r['sample_count']==3*m*2
            assert r['zero_work_muscles']==0 and r['zero_resource_muscles']==0
            assert r['restore_verified']
def test_streaming_exact_trial_count():
    rows=run(7,10,2,19,chunk=3)
    assert all(r['trials']==7 for r in rows)
