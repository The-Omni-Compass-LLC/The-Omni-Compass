#!/usr/bin/env bash
# One receipt per plant. Fails closed when the host for that plant is not on this machine.
# Does not invent a watt, a joint speed, or a feeder amp.
set -u
PLANT="${PLANT:-compute}"
OUT="${OUT:-plant-out/$PLANT}"
mkdir -p "$OUT"
STAMP="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

write_not_hosted() {
  local why="$1"
  cat > "$OUT/PLANT_RECEIPT.json" <<EOF
{
  "plant": "$PLANT",
  "status": "NOT_HOSTED",
  "reason": "$why",
  "stamp": "$STAMP",
  "claim": "no number from this plant is claimed",
  "restore": "not applicable; no lever was written"
}
EOF
  echo "NOT_HOSTED $PLANT $why" | tee "$OUT/FAIL.txt"
}

case "$PLANT" in
  compute)
    if ! command -v nvidia-smi >/dev/null 2>&1; then
      write_not_hosted "no nvidia-smi on this machine"
      exit 2
    fi
    exec bash scripts/one_box_receipt.sh
    ;;
  facility)
    if [ ! -r "${FACILITY_METER:-/no/such/rack-meter}" ]; then
      write_not_hosted "no rack meter path; set FACILITY_METER to a readable kW source on a real hall host"
      exit 0
    fi
    write_not_hosted "meter path exists but no facility write adapter is connected in this package"
    exit 0
    ;;
  machine)
    if [ ! -r "${MACHINE_METER:-/no/such/servo}" ]; then
      write_not_hosted "no servo or PLC port; set MACHINE_METER on the machine host"
      exit 0
    fi
    write_not_hosted "port exists but no motion write adapter is connected in this package"
    exit 0
    ;;
  grid)
    if [ ! -r "${GRID_METER:-/no/such/feeder}" ]; then
      write_not_hosted "no feeder or battery meter; set GRID_METER on the grid host"
      exit 0
    fi
    write_not_hosted "meter path exists but no grid write adapter is connected in this package"
    exit 0
    ;;
  *)
    write_not_hosted "unknown plant"
    exit 2
    ;;
esac
