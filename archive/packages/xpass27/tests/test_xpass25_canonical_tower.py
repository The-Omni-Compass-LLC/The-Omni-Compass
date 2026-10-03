import csv,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
def test_tower_count_unique():
 rows=list(csv.DictReader(open(R/'organism/referee_canonical_v3/CANONICAL_656_TOWER.csv'))); assert len(rows)==656; assert len({r['canonical_name'] for r in rows})==656
def test_status():
 s=json.load(open(R/'XPASS25_STATUS.json')); assert s['canonical_benchmark_target_N']==656 and s['engine_modified'] is False
def test_no_supporting_in_tower():
 rows=list(csv.DictReader(open(R/'organism/referee_canonical_v3/CANONICAL_656_TOWER.csv'))); assert all(r['xpass25_disposition']=='CANONICAL_BENCHMARK_TARGET' for r in rows)
