# Section 3: Remotes & GitHub

## What Are Remotes?

A **remote** is a copy of your repository hosted on a server (like GitHub, GitLab, or Bitbucket). Remotes enable collaboration — multiple developers can push and pull changes to a shared repository.

When you clone a repo, Git automatically sets up a remote called **`origin`** that points to the URL you cloned from.

## Remote Commands

### View remotes

```bash
# List remotes
git remote

# List remotes with URLs
git remote -v
```

### Add a remote

```bash
git remote add origin https://github.com/user/repo.git
```

### Remove or rename a remote

```bash
git remote remove old-remote
git remote rename old-name new-name
```

## Push, Pull, and Fetch

### `git push` — Upload your commits

```bash
# Push current branch to origin
git push origin main

# Set upstream and push (so future pushes just need `git push`)
git push -u origin main

# Push all branches
git push --all origin
```

### `git pull` — Download and merge remote changes

```bash
# Pull latest changes from origin/main
git pull origin main

# Pull with rebase instead of merge (cleaner history)
git pull --rebase origin main
```

`git pull` = `git fetch` + `git merge`

### `git fetch` — Download without merging

```bash
# Fetch all remote changes
git fetch origin

# See what changed before merging
git log HEAD..origin/main --oneline
```

Use `fetch` when you want to **review** remote changes before integrating them.

## Collaboration on GitHub

### Forking

A **fork** is your personal copy of someone else's repository on GitHub.

1. Click "Fork" on the GitHub repo page
2. Clone your fork: `git clone https://github.com/YOUR-USERNAME/repo.git`
3. Add the original repo as "upstream":
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/repo.git
   ```
4. Keep your fork up to date:
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

### Pull Requests (PRs)

A Pull Request is a proposal to merge your changes into another branch or repository.

**The PR workflow:**

```
1. Fork or branch  →  2. Make changes  →  3. Push  →  4. Open PR  →  5. Review  →  6. Merge
```

**Steps:**

1. Create a branch for your feature:
   ```bash
   git switch -c fix-typo
   ```
2. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Fix typo in README"
   ```
3. Push the branch to GitHub:
   ```bash
   git push -u origin fix-typo
   ```
4. Go to GitHub and click "Compare & pull request"
5. Write a clear title and description
6. Request reviewers and wait for feedback
7. Once approved, merge the PR

### Cloning with SSH vs HTTPS

| Method | URL Format | Authentication |
|--------|-----------|----------------|
| HTTPS | `https://github.com/user/repo.git` | Username + token |
| SSH | `git@github.com:user/repo.git` | SSH key pair |

SSH is recommended for regular use — no need to type credentials each time.

**Set up SSH:**
```bash
# Generate a key pair
ssh-keygen -t ed25519 -C "your.email@example.com"

# Copy the public key
cat ~/.ssh/id_ed25519.pub

# Add it to GitHub: Settings → SSH and GPG keys → New SSH key
```

## Exercises

### Exercise 1: Connect a Local Repo to GitHub

1. Create a new repo on GitHub (don't initialize with README)
2. In your local repo, add the remote:
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/repo-name.git
   ```
3. Push your code:
   ```bash
   git push -u origin main
   ```
4. Verify on GitHub that your files appear

### Exercise 2: Practice the PR Workflow

1. Create a new branch: `git switch -c update-collab-example`
2. Modify `collab-example.py` — add your name to the contributors list
3. Commit and push:
   ```bash
   git add collab-example.py
   git commit -m "Add my name to contributors"
   git push -u origin update-collab-example
   ```
4. Open a Pull Request on GitHub
5. (If working with a partner) Request a review

### Exercise 3: Fetch and Inspect

1. Ask a partner to push a change, or make a change directly on GitHub
2. Fetch without merging: `git fetch origin`
3. Compare: `git log HEAD..origin/main --oneline`
4. When ready, merge: `git merge origin/main`

---

**Next:** [Section 4 — Workflows](../04-workflows/README.md)
