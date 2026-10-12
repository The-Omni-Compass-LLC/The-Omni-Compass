# The bill on Google Cloud: setting it up, click by click

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This connects GitHub to a Google Cloud account so two workflows can run the same tests Azure runs:

- **`gke-metered`**: a real Google Kubernetes Engine cluster, native Kubernetes (with Google's own cluster autoscaler)
  against the same with Omni-Compass on top, the machines Google bills counted every 15 seconds, the organisms with the
  cluster inside at 1, 10, 100 and 1,000 copies (`organism`, `organism_scale`), everything deleted at the end. The same
  design as Azure's `aks-metered` (`docs/K8S_COMPASS_PREREGISTRATION.md`).
- **`cloud-organism`** with `cloud` = `gcp`: the big organisms (the whole tower and the four stacked at 1,000 copies, the
  real cluster inside) on one rented 8-processor machine, the same test Azure's `big-organism-detached` runs.

About fifteen minutes, once. New accounts get **$300 of free credit for 90 days**; Google does not charge the card during the
free trial.

## 1. A Google Cloud account with the free credit

1. On the laptop, open **cloud.google.com/free** and click **Get started for free**.
2. Sign in with a Google account (a Gmail address works), or make one.
3. Choose the country, tick the terms, click **Continue**.
4. Enter a card. Google uses it to confirm who you are; the $300 credit is used first.
5. Click **Start my free trial**. The Google Cloud console opens (**console.cloud.google.com**).
6. **Turn on the full account** (the credit stays and is still used first; the free trial otherwise limits how many
   machines run at once and refuses GPUs): at the top of the console click **Activate** (or open the menu ☰, **Billing**,
   then **Upgrade** / **Activate full account**) and confirm.

## 2. A project for Omni-Compass

1. At the top left of the console, click the project picker (next to "Google Cloud").
2. Click **New project**. Name: `omni-compass`. Click **Create**.
3. When it is made, pick it in the project picker. Under the name you see its **Project ID** (for example
   `omni-compass-123456`). Write it down: it is the second secret below.

## 3. Google's own terminal (nothing to install)

1. At the top right of the console, click the **>_** icon (**Activate Cloud Shell**).
2. A terminal opens at the bottom of the page. If it asks to authorize, click **Authorize**.

## 4. One paste: a login for GitHub

Paste this whole block into that terminal and press **Enter** (it takes about a minute):

```bash
P=$(gcloud config get-value project)
gcloud services enable container.googleapis.com compute.googleapis.com iam.googleapis.com
gcloud iam service-accounts create omni-compass-github --display-name "Omni-Compass GitHub"
for r in roles/container.admin roles/compute.admin roles/iam.serviceAccountUser; do
  gcloud projects add-iam-policy-binding "$P" --member "serviceAccount:omni-compass-github@$P.iam.gserviceaccount.com" --role "$r" --quiet >/dev/null
done
gcloud iam service-accounts keys create key.json --iam-account "omni-compass-github@$P.iam.gserviceaccount.com"
cat key.json; rm key.json
```

It prints a block that starts with `{` and ends with `}`. Select all of it, from `{` to `}`, and copy it. That block is a
password for this one purpose: never paste it anywhere but the GitHub secret below. (If the project picker showed no
project, run `gcloud config set project YOUR-PROJECT-ID` first.)

## 5. Put the two secrets in GitHub

1. Open the repository on GitHub, click **Settings** (the repository's tab, at the top right), then on the left
   **Secrets and variables**, then **Actions**.
2. **New repository secret**. Name: `GCP_CREDENTIALS`. Secret: paste the whole block from step 4. **Add secret**.
3. **New repository secret**. Name: `GCP_PROJECT`. Secret: the Project ID from step 2. **Add secret**.

That is all. Tell Claude the two secrets are in; it starts the runs on the newest engine (branch `v5`) and reports each
result before anything goes up.

## 6. What it costs

Google's list prices (us-central1, on demand): a worker of the Kubernetes test (`e2-standard-2`) about $0.067 an hour, up to
4 workers an arm, about $5 to $15 for a full five-repetition set; the big-organism machine (`e2-standard-8`) about $0.27 an
hour, about $10 for its 39-hour ceiling. All of it comes out of the $300 credit first. Every cluster and machine is
deleted when its run ends, whatever happens.

## 7. Afterwards

To remove GitHub's access: in the console menu ☰ **IAM & Admin**, **Service Accounts**, tick **omni-compass-github**,
**Delete**; and delete the two secrets in GitHub.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
