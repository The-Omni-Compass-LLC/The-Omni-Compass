# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The monitor wall as a Grafana dashboard: one panel a monitor, each on the open-source feed that carries it live.

The live engine's monitors (docs/engine/monitors.json) are, in the founder's words, nothing more than a Grafana-type dashboard
wired to the organism. This writes that dashboard (deploy/grafana/omni-compass-wall.json, Grafana's dashboard model, schema 39):
a monitor with a Prometheus expression becomes a panel on that expression (the datasource a variable, ${DS_PROMETHEUS}); a
monitor the page computes from the repository's tables, or from its own clock, becomes a text panel saying so and where the
number lives. Beside deploy/grafana/omni-compass.json (the governor's own seventeen panels on tools/omni_exporter.py) it is the
whole wall for an operator's Grafana. The page embeds the same model and offers it for download; the builder writes the file.
Every panel carries its monitor's number on the page, its order of appearance, and the panels run left to right, then the next row.

  python3 docs/engine/export_grafana.py [OUT.json]      (default: deploy/grafana/omni-compass-wall.json)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REG = HERE / "monitors.json"
PAGE = HERE / "OMNI_COMPASS_LIVE_ENGINE.html"
OUT = ROOT / "deploy" / "grafana" / "omni-compass-wall.json"
W, H, COLS = 12, 8, 2


def page_order() -> list:
    """The page's canvases in their order of appearance: the monitors' numbers, as the page itself counts them."""
    import re
    if not PAGE.exists():
        return []
    body = re.sub(r"<script[^>]*>.*?</script>", "", PAGE.read_text(encoding="utf-8"), flags=re.S)
    return [m.group(1) for m in re.finditer(r'<canvas\b[^>]*\bid="([^"]+)"', body)]


def dashboard(reg: dict) -> dict:
    panels = []
    order = {cid: i for i, cid in enumerate(page_order())}   # every panel numbered as the page numbers its monitor, laid out left to right
    for i, m in enumerate(sorted(reg["monitors"], key=lambda m: order.get(m["id"], len(order)))):
        n = i + 1
        x, y = (i % COLS) * W, (i // COLS) * H
        title = f"{n} · {m['name']}"
        base = {"id": n, "title": title, "gridPos": {"x": x, "y": y, "w": W, "h": H},
                "description": f"{m['what']} Evidence class {m['cls']}; on the live engine: {m['status']}. Feed: {m['feed']['exporter']}."
                               + (f" Awaiting: {m['awaiting']}." if m.get("awaiting") else "")}
        if m["feed"]["promql"]:
            panels.append({**base, "type": m["grafana"]["type"] if m["grafana"]["type"] in ("timeseries", "stat", "bargauge", "heatmap", "table") else "timeseries",
                           "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                           "fieldConfig": {"defaults": {"unit": m["grafana"].get("unit") or "short"}, "overrides": []},
                           "targets": [{"refId": chr(65 + j), "expr": e, "legendFormat": m["feed"]["metrics"][j] if j < len(m["feed"]["metrics"]) else e}
                                       for j, e in enumerate(m["feed"]["promql"])]})
        else:
            panels.append({**base, "type": "text", "options": {"mode": "markdown", "content":
                           f"**{m['name']}** ({reg['layers'].get(m['layer'], m['layer'])}).\n\n{m['what']}\n\nSource: {m['feed']['exporter']}. "
                           f"No Prometheus series carries this panel: the live engine draws it from the repository's own records or from its own clock; "
                           f"this panel marks its place on the wall (monitor {n})."}})
    return {"uid": "omni-compass-wall", "title": "Omni-Compass: the monitor wall", "tags": ["omni-compass", "wall"], "timezone": "utc", "schemaVersion": 39, "version": 1,
            "editable": True, "graphTooltip": 1, "time": {"from": "now-6h", "to": "now"}, "refresh": "30s",
            "templating": {"list": [{"name": "DS_PROMETHEUS", "label": "Prometheus", "type": "datasource", "query": "prometheus", "current": {}, "hide": 0}]},
            "links": [{"title": "The governor's own screen", "type": "dashboards", "tags": ["omni-compass"], "asDropdown": False},
                      {"title": "The live engine", "type": "link", "url": "https://github.com/The-Omni-Compass-LLC/The-Omni-Compass/blob/main/docs/engine/OMNI_COMPASS_LIVE_ENGINE.html"}],
            "panels": panels,
            "__notice": "© 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com"}


def main(out: str | None = None) -> dict:
    reg = json.loads(REG.read_text(encoding="utf-8"))
    d = dashboard(reg)
    p = Path(out) if out else OUT
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return d


if __name__ == "__main__":
    d = main(sys.argv[1] if len(sys.argv) > 1 else None)
    print(f"{len(d['panels'])} panels, {sum(1 for p in d['panels'] if p['type'] != 'text')} on Prometheus series")
