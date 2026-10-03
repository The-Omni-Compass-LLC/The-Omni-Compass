# Drop on branch claude/kubernetes-clusters-docker-stack-gp26ve

Copy:
  scripts/kind_chaos.sh
  scripts/kind_fairness.sh
  deploy/kind/two-app-fairness.yaml
  .github/workflows/live-kind-chaos.yml
  .github/workflows/live-kind-fairness.yml

chmod +x scripts/kind_chaos.sh scripts/kind_fairness.sh

One commit message to start BOTH plus the already-built rungs:

  add chaos and fairness [chaos] [fair] [full] [shadow]

Or smaller:
  start chaos [chaos]
  start fairness [fair]
  start full and shadow [full] [shadow]

I cannot git push from Grok (403). You add the files on GitHub or Claude Thursday does.
