#!/usr/bin/env python3
from pathlib import Path
import csv

# Breadth first, then recursive replication of the COMPLETE organism.
# N is discovered from the admitted canonical registry and is never hard-coded.
PREFIX=(1,10,100)
REPLICATION=(1,10,100,1000,10000,100000,1000000)

def catalog_count(path: Path)->int:
    with path.open(newline='') as f:
        return sum(1 for _ in csv.DictReader(f))

def breadth_ladder(final_count:int):
    if final_count < 1:
        raise ValueError('final_count >= 1')
    # Owner rule: show only meaningful cumulative breadth rungs below N.
    # No arbitrary 500/1000 rung. Once complete breadth N is reached,
    # scaling is replication of the complete N-muscle organism.
    return tuple([x for x in PREFIX if x < final_count] + [final_count])

def recursive_scale_ladder(final_count:int, factors=REPLICATION):
    if final_count < 1:
        raise ValueError('final_count >= 1')
    return tuple(final_count * f for f in factors)

def benchmark_ladder(final_count:int):
    b=breadth_ladder(final_count)
    s=recursive_scale_ladder(final_count)
    # N occurs at the end of breadth and beginning of scale; emit once.
    return b + s[1:]
