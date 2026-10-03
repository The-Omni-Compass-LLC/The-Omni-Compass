import importlib.util
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('x20',ROOT/'collective/xpass20_matrix_lab.py'); x20=importlib.util.module_from_spec(spec);spec.loader.exec_module(x20)
def test_catalog_640(): assert len(x20.load_catalog(ROOT))==640
def test_exact_active_muscles():
 for m in (1,10,100,500,640):
  ids,c=x20.assignment(max(1000,m),m); assert len(c)==m and np.all(c>0) and len(np.unique(ids))==m
def test_population_smaller_than_breadth_rejected():
 import pytest
 with pytest.raises(ValueError): x20.assignment(100,640)
def test_paired_arms_only(): assert x20.ARMS==('NATIVE','OMNI_OVER_NATIVE')
def test_640_all_simultaneous_smoke():
 for arm in x20.ARMS:
  r=x20.run_arm(arm,640,640,2,123); assert r['muscles_active']==640 and r['muscles_with_zero_work']==0 and r['muscles_with_zero_resource']==0 and r['restore_verified']
