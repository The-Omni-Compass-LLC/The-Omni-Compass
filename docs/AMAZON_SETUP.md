# The bill on Amazon Web Services: setting it up, click by click

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This connects GitHub to an Amazon Web Services (AWS) account so two workflows can run the same tests Azure runs:

- **`eks-metered`**: a real Amazon Elastic Kubernetes Service cluster, native Kubernetes (with its own cluster autoscaler)
  against the same with Omni-Compass on top, the machines Amazon bills counted every 15 seconds, the organisms with the
  cluster inside at 1, 10, 100 and 1,000 copies (`organism`, `organism_scale`), everything deleted at the end. The same
  design as Azure's `aks-metered` (`docs/K8S_COMPASS_PREREGISTRATION.md`).
- **`cloud-organism`** with `cloud` = `aws`: the big organisms (the whole tower and the four stacked at 1,000 copies, the
  real cluster inside) on one rented 8-processor machine, the same test Azure's `big-organism-detached` runs.

About fifteen minutes, once. New accounts get **$100 of credit at sign-up and up to $100 more** for trying services, used
before the card.

## 1. An AWS account

1. On the laptop, open **aws.amazon.com/free** and click **Create a Free Account** (or **Create an AWS account**).
2. Enter an e-mail address and an account name (`Omni-Compass`), click **Verify email address**, and type the code Amazon
   e-mails you.
3. Choose a password for the root user.
4. Contact information: **Business** (The Omni-Compass LLC) or **Personal**, the address and phone.
5. **Choose the Paid plan** if Amazon asks you to pick a plan. Your credits still pay first; the Free plan blocks services
   these tests need (the Kubernetes service among them).
6. Enter a card, then confirm the phone number with the code Amazon sends.
7. Support plan: **Basic support - Free**. Click **Complete sign up**, then **Go to the AWS Management Console** and sign in
   as the root user.

## 2. A login for GitHub (an IAM user)

1. In the search bar at the top of the console type **IAM** and open it.
2. On the left, **Users**, then **Create user**. User name: `omni-compass-github`. Do **not** tick console access.
   **Next**.
3. **Attach policies directly**. Tick **AdministratorAccess** (the tests build whole Kubernetes clusters, which needs EKS,
   EC2, CloudFormation and roles; this user is used only by GitHub, and you delete it when the tests are done). **Next**,
   **Create user**.
4. Click the new user **omni-compass-github**, open the **Security credentials** tab, and under **Access keys** click
   **Create access key**.
5. Choose **Application running outside AWS** (or **Other**), **Next**, **Create access key**.
6. The page shows an **Access key** (starts with `AKIA`) and a **Secret access key**. Keep the page open for the next step;
   the secret is shown only once. These two are passwords for this one purpose: never paste them anywhere but GitHub.

## 3. Put the two secrets in GitHub

1. Open the repository on GitHub, click **Settings** (the repository's tab, at the top right), then on the left
   **Secrets and variables**, then **Actions**.
2. **New repository secret**. Name: `AWS_ACCESS_KEY_ID`. Secret: the Access key. **Add secret**.
3. **New repository secret**. Name: `AWS_SECRET_ACCESS_KEY`. Secret: the Secret access key. **Add secret**.

That is all. Tell Claude the two secrets are in; it starts the runs on the newest engine (branch `v5`) and reports each
result before anything goes up.

## 4. What it costs

Amazon's list prices (us-east-1, on demand): a worker of the Kubernetes test (`m5.large`) about $0.096 an hour, up to 4
workers an arm, plus about $0.10 an hour for each cluster's control plane, about $10 to $25 for a full five-repetition set;
the big-organism machine (`m6i.2xlarge`) about $0.38 an hour, about $15 for its 39-hour ceiling. The credits pay first.
Every cluster and machine is deleted when its run ends, whatever happens.

If Amazon refuses a machine for "vCPU limit" (new accounts start with a small limit): in the console search **Service
Quotas**, open **Amazon Elastic Compute Cloud (Amazon EC2)**, **Running On-Demand Standard (A, C, D, H, I, M, R, T, Z)
instances**, **Request increase at account level**, ask for 64, **Request**. Amazon usually answers within a day.

## 5. Afterwards

To remove GitHub's access: in IAM, **Users**, tick **omni-compass-github**, **Delete**; and delete the two secrets in
GitHub.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
