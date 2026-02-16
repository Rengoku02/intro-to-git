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

Use the `git-bio-project` repo you've been building in the previous sections.

### Exercise 1: Push Your Bio Project to GitHub

1. Go to GitHub and create a new repository called `git-bio-project` (don't initialize with a README)
2. In your local `git-bio-project` directory, add the remote:
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/git-bio-project.git
   ```
3. Push your code:
   ```bash
   git push -u origin main
   ```
4. Verify on GitHub that your files (`count_sequences.py`, `gc_content.py`) appear

### Exercise 2: Practice the PR Workflow

1. Create a new branch: `git switch -c add-contributors`
2. Create a `contributors.txt` file and add your name:
   ```
   # Contributors
   - Your Name
   ```
3. Commit and push:
   ```bash
   git add contributors.txt
   git commit -m "Add contributors file"
   git push -u origin add-contributors
   ```
4. Go to GitHub and click "Compare & pull request"
5. Write a title and description, then merge the PR
6. Pull the merged changes locally: `git pull origin main`

### Exercise 3: Fetch and Inspect

1. Go to your repo on GitHub and edit `contributors.txt` directly in the browser (click the pencil icon) — add a second name or a date
2. **Don't pull yet.** Instead, fetch without merging: `git fetch origin`
3. Compare what changed: `git log HEAD..origin/main --oneline`
4. When ready, merge: `git merge origin/main`
5. Verify the change is in your local file

---

**Next:** [Section 4 — Workflows](../04-workflows/README.md)
