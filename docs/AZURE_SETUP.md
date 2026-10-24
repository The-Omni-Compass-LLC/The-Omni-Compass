# The bill on a real cloud: setting up Azure, click by click

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> Evaluation and Simulation use only; any other use requires a signed, paid Omni-Compass Enterprise License. See
> [`LICENSE`](../LICENSE).

This connects GitHub to an Azure account so the workflow `aks-metered` can build a real Azure Kubernetes Service
cluster, run native Kubernetes (with Azure's own cluster autoscaler) against the same with Omni-Compass on top, count
the machines Azure bills every 15 seconds, and delete everything when it is done. The design is written before the
run in `docs/K8S_COMPASS_PREREGISTRATION.md`, "The bill on a real cloud". It costs about USD 10 to 30 of Azure time; a new
account's free credit usually covers it. About ten minutes, once.

## 1. An Azure account

1. Open **azure.microsoft.com/free** and click **Start free** (or **Try Azure for free**).
2. Sign in with a Microsoft account, or make one.
3. Fill in the form. Azure asks for a card to confirm who you are; the free credit is used first.
4. When it says the account is ready, go to **portal.azure.com**.

## 2. Azure's own terminal (nothing to install)

1. In the Azure portal, at the top of the page, click the **>_** icon (Cloud Shell), to the right of the search bar.
2. If it asks, choose **Bash** (not PowerShell).
3. If it asks about storage, choose **No storage account required** (or accept the default and **Create**).
4. A black terminal opens at the bottom of the page.

## 3. One line: a login for GitHub

Paste this line into that terminal and press **Enter**:

```bash
az ad sp create-for-rbac --name omni-compass-github --role contributor --scopes /subscriptions/$(az account show --query id -o tsv) --sdk-auth
```

It prints a block of text that starts with `{` and ends with `}`. Select all of it, from `{` to `}`, and copy it.
That block is a password for this one purpose; never paste it anywhere but the GitHub secret below.

## 4. Put it in GitHub

1. Open the repository on GitHub.
2. Click **Settings** (the tab at the top right of the repository, not your account settings).
3. On the left: **Secrets and variables**, then **Actions**.
4. Click **New repository secret**.
5. **Name:** `AZURE_CREDENTIALS`
6. **Secret:** paste the whole block from step 3.
7. Click **Add secret**.

## 5. Run it

**Actions** tab, then **aks-metered** on the left, then **Run workflow**, then the green **Run workflow** button. The
defaults are the preregistered design (5 repetitions, native and native with Omni-Compass on top, 900 measured seconds,
Standard_D2s_v4 in eastus, the governor at the tune-down on the machines alone: the pods exactly native's, so the bill can
only fall or stay). About 6 hours on GitHub. Each cluster is deleted when its arm ends, and the resource group at the end of every
repetition whatever happens, so nothing keeps billing.

If Azure answers **quota exceeded**: in the portal, search **Subscriptions**, open yours, and upgrade it to
**Pay-As-You-Go** (the credit stays), or ask for a quota of 10 vCPUs for the DSv4 family in the region.

## 6. Afterwards

The result is the job `aggregate`'s receipt: billed machine-hours and the bill at list price, native against native
with Omni-Compass on top, beside response time, failures and CPU, each with its 95% interval. To remove GitHub's
access when you are done: in the Azure portal search **App registrations**, open **omni-compass-github**, **Delete**;
and delete the `AZURE_CREDENTIALS` secret in GitHub.

## 7. When Azure's check says the key is not whole

Every Azure set, and the conductor's own check at no cost (the run **cloud-check azure** on the **Actions** tab), reads the
shape of `AZURE_CREDENTIALS` before Azure's login and says what is wrong without printing a character of it: that it does not
start with `{`, that it holds a client secret's value alone, that it was cut short, or which field is missing. Store it again,
whole:

1. In the Azure portal, click **>_** (Cloud Shell) and choose **Bash**, as in section 2.
2. Paste the one line of section 3 again and press **Enter**. It prints a new block that starts with `{` and ends with `}`.
3. Select all of it, from `{` to `}`, and copy it.
4. On GitHub, open the repository, then **Settings**, then **Secrets and variables**, then **Actions**.
5. Beside `AZURE_CREDENTIALS`, click the pencil (**Update**).
6. Paste the whole block as the new value and click **Update secret**.
7. To retire every older password of the same login: in the Azure portal search **App registrations**, open
   **omni-compass-github**, then **Certificates & secrets**, and delete every client secret but the newest.

The conductor runs Azure's check again within the hour, and the sets start on their own once it passes. Nothing is built and
nothing is billed while it fails.

## 8. The second way in: the sign-in without a password (OIDC)

Since 23 October, evening, the repository also holds a sign-in with no password at all: three IDs (`AZURE_CLIENT_ID`,
`AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`) and a rule in Azure that trusts this repository's own runs. The inventory
(`azure-inventory.yml`) uses it. On 24 October it was refused: Azure answered that no trust rule matched the name GitHub
presented (`AADSTS700213`), because GitHub now presents this repository by its ID numbers, and the rule in Azure names it the
older way. One rule with the exact name makes it work:

1. In the Azure portal, search **App registrations** and open the app whose **Application (client) ID** is the one stored as
   `AZURE_CLIENT_ID`.
2. Click **Certificates & secrets**, then the tab **Federated credentials**, then **+ Add credential**.
3. **Federated credential scenario**: choose **Other issuer**.
4. **Issuer**: `https://token.actions.githubusercontent.com`
5. **Subject identifier** (type it exactly, or copy it from this page): 
   `repo:The-Omni-Compass-LLC@334396871/The-Omni-Compass@1390458092:ref:refs/heads/main`
6. **Name**: `github-main`. Leave **Audience** at `api://AzureADTokenExchange`. Click **Add**.
7. The app needs a role on the subscription: **Subscriptions**, the subscription, **Access control (IAM)**, **Add role
   assignment**, **Reader** for the inventory.

The benchmark sets keep the key of section 3. A sign-in without a password holds for about an hour and cannot renew itself
inside a job, while one Azure repetition runs about 70 minutes and must still be signed in at its end to delete what it built;
a lapsed sign-in there could leave machines running and billing. So the sets, and Azure's $0 check that clears them, read only
`AZURE_CREDENTIALS`, and nothing is started while that key is not whole (section 7).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
