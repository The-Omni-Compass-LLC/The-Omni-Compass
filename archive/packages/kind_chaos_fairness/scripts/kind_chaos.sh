#!/usr/bin/env bash
# Kill Omni mid-loop (SIGKILL, no graceful kill file) then run the restore one-shot.
# Pass: HPA target is 50 after the watchdog one-shot. Fail if not.
set -euo pipefail
OUT_DIR="${OUT_DIR:-kind_chaos_out}"; PHASE_S="${PHASE_S:-180}"; mkdir -p "$OUT_DIR"

kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
kubectl -n kube-system patch deployment metrics-server --type=json \
  -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]'
kubectl -n kube-system rollout status deployment/metrics-server --timeout=300s
kubectl apply -f deploy/kind/demo.yaml
kubectl rollout status deployment/php-apache --timeout=300s
kubectl run load-generator --image=busybox:1.36 --restart=Never -- /bin/sh -c \
  "while true; do for i in \$(seq 1 20); do wget -q -O- http://php-apache >/dev/null; done; sleep \$((RANDOM % 3)); done" || true
for i in $(seq 1 30); do kubectl top nodes >/dev/null 2>&1 && break; sleep 10; done

before=$(kubectl get hpa php-apache -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}')
echo "hpa_target_before=$before" | tee "$OUT_DIR/snapshot.txt"
test "$before" = "50"

echo "== Omni target mode (will be killed mid-loop)"
python -m omni_controller.controller --mode target --interval 15 --iterations 40 \
  --audit "$OUT_DIR/audit_live.jsonl" --kill-file "$OUT_DIR/kill" &
OMNI_PID=$!
echo "omni_pid=$OMNI_PID" | tee "$OUT_DIR/omni_pid.txt"
sleep "$PHASE_S"
if kill -0 "$OMNI_PID" 2>/dev/null; then
  echo "sending SIGKILL to $OMNI_PID" | tee "$OUT_DIR/kill_method.txt"
  kill -9 "$OMNI_PID" || true
  wait "$OMNI_PID" || true
else
  echo "omni already exited before SIGKILL" | tee "$OUT_DIR/kill_method.txt"
fi
mid=$(kubectl get hpa php-apache -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}' || echo missing)
echo "hpa_target_after_sigkill=$mid" | tee "$OUT_DIR/after_death.txt"

echo "== Watchdog one-shot restore (same kill path as kind_pilot, after dirty death)"
touch "$OUT_DIR/kill"
python -m omni_controller.controller --mode target --iterations 1 \
  --audit "$OUT_DIR/audit_restore.jsonl" --kill-file "$OUT_DIR/kill"
restored=$(kubectl get hpa php-apache -o jsonpath='{.spec.metrics[0].resource.target.averageUtilization}')
echo "restored target: $restored" | tee "$OUT_DIR/kill_switch.txt"
test "$restored" = "50"
echo "CHAOS_PASS restored_to=50 after_sigkill=$mid" | tee "$OUT_DIR/score.txt"
