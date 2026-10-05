# The bill on a real cloud: setting up Azure, click by click

> Evaluation and simulation use only; any other use requires a signed, paid Omni-Compass Enterprise License. See
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
defaults are the preregistered design (5 repetitions, native / compass / omni, 900 measured seconds, Standard_D2s_v5 in
eastus). About 6 hours on GitHub. Each cluster is deleted when its arm ends, and the resource group at the end of every
repetition whatever happens, so nothing keeps billing.

If Azure answers **quota exceeded**: in the portal, search **Subscriptions**, open yours, and upgrade it to
**Pay-As-You-Go** (the credit stays), or ask for a quota of 10 vCPUs for the Dv5 family in the region.

## 6. Afterwards

The result is the job `aggregate`'s receipt: billed machine-hours and the bill at list price, native against native
with Omni-Compass on top, beside response time, failures and CPU, each with its 95% interval. To remove GitHub's
access when you are done: in the Azure portal search **App registrations**, open **omni-compass-github**, **Delete**;
and delete the `AZURE_CREDENTIALS` secret in GitHub.

---

*Evaluation and simulation use only. Copyright (c) 2026 The Omni-Compass LLC. Commercial use, commercialization or
monetization of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC.
Patent applications, copyright registrations and trademark applications filed in the United States. See `LICENSE` and
`NOTICE` at the root of this repository.*
