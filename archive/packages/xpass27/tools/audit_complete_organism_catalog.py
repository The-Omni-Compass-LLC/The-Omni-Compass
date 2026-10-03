#!/usr/bin/env python3
import csv,json,collections,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CAT=ROOT/'muscles'/'FULL_TOWER_640.csv'
OUT=ROOT/'organism'/'CATALOG_AUDIT_CURRENT.json'
rows=list(csv.DictReader(CAT.open(newline='')))
names=[r['canonical_name'].strip() for r in rows]
fams=collections.Counter(r['family'].strip() for r in rows)
dups=sorted(k for k,v in collections.Counter(names).items() if v>1)
report={
 'historical_checkpoint_file':str(CAT.relative_to(ROOT)),
 'historical_checkpoint_rows':len(rows),
 'unique_canonical_names':len(set(names)),
 'duplicate_canonical_names':dups,
 'family_count':len(fams),
 'family_sizes':dict(sorted(fams.items())),
 'uniform_family_size': len(set(fams.values()))==1,
 'uniform_family_size_value': next(iter(fams.values())) if len(set(fams.values()))==1 else None,
 'audit_warning':'Uniform family sizing is a catalog-construction signal, not evidence that the organism is complete. Preserve this file as a checkpoint; discover N independently.',
 'sha256':hashlib.sha256(CAT.read_bytes()).hexdigest(),
 'complete_organism_N':'OPEN_DISCOVERY',
 'engine_change':'NONE'
}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
