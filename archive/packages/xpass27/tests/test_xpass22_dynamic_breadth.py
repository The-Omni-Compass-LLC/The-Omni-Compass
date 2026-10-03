from organism.breadth_ladder import breadth_ladder, recursive_scale_ladder, benchmark_ladder

def test_breadth_is_importance_progression_then_complete_N():
    assert breadth_ladder(640)==(1,10,100,640)
    assert breadth_ladder(1184)==(1,10,100,1184)
    assert breadth_ladder(487)==(1,10,100,487)
    assert breadth_ladder(73)==(1,10,73)
    assert breadth_ladder(7)==(1,7)

def test_recursive_scale_replicates_complete_organism_not_new_muscle_types():
    assert recursive_scale_ladder(640)[:5]==(640,6400,64000,640000,6400000)
    assert recursive_scale_ladder(1184)[:4]==(1184,11840,118400,1184000)

def test_full_benchmark_ladder():
    assert benchmark_ladder(640)[:8]==(1,10,100,640,6400,64000,640000,6400000)
