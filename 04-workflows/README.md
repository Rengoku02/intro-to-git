# Section 4: Workflows & Beyond

## Why Workflows Matter

A Git workflow is an agreed-upon set of rules for how a team uses branches, merges, and releases. Without one, collaboration becomes chaotic. With one, everyone knows where to commit, how to review, and when to deploy.

## Common Workflows

### 1. GitHub Flow

The simplest workflow — great for teams that deploy frequently.

**Rules:**
- `main` is always deployable
- Create a branch for every change
- Open a Pull Request for review
- Merge to `main` after approval
- Deploy from `main`

```
main:       A---B-------E---F
                 \     /
feature:          C---D
                  (PR)
```

**Best for:** Web apps, SaaS products, small teams, continuous deployment.

### 2. Git Flow

A more structured workflow with dedicated branches for features, releases, and hotfixes.

**Branches:**
- `main` — production-ready code
- `develop` — integration branch for features
- `feature/*` — individual feature branches (branch from `develop`)
- `release/*` — release preparation (branch from `develop`)
- `hotfix/*` — emergency production fixes (branch from `main`)

```
main:       A-----------G---H (hotfix)
             \         /   /
develop:      B---C---D---E---F
                   \     /
feature:            X---Y
```

**Best for:** Projects with scheduled releases, larger teams, versioned software.

### 3. Trunk-Based Development

Everyone commits to `main` (the "trunk") frequently. Short-lived branches are optional and last less than a day.

**Rules:**
- Commit to `main` directly or via very short-lived branches
- Keep commits small and incremental
- Use feature flags to hide incomplete work
- Continuous integration runs on every commit

```
main: A---B---C---D---E---F---G
          |       |
          (small, frequent commits)
```

**Best for:** Experienced teams, CI/CD-heavy projects, Google/Meta-style engineering.

## Comparing Workflows

| Aspect | GitHub Flow | Git Flow | Trunk-Based |
|--------|-----------|----------|-------------|
| Complexity | Low | High | Low |
| Branch lifespan | Days | Days–Weeks | Hours |
| Release process | Continuous | Scheduled | Continuous |
| Team size | Small–Medium | Medium–Large | Any |
| Best for | Web apps | Versioned software | CI/CD-heavy projects |

## Tags and Releases

Tags mark specific commits as important — typically used for version releases.

### Creating tags

```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag (recommended — includes metadata)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Tag a specific commit
git tag -a v1.0.0 abc1234 -m "Release version 1.0.0"
```

### Working with tags

```bash
# List all tags
git tag

# Push a tag to remote
git push origin v1.0.0

# Push all tags
git push origin --tags

# Delete a tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

### GitHub Releases

On GitHub, you can create a **Release** from a tag:
1. Go to your repo → Releases → "Create a new release"
2. Choose a tag
3. Write release notes
4. Optionally attach binary files

---

## git stash — Save Work Without Committing

Stash lets you temporarily shelve changes so you can switch context (e.g., switch branches) without committing half-done work.

```bash
# Stash your current changes
git stash

# Stash with a descriptive message
git stash push -m "WIP: login form validation"

# List all stashes
git stash list

# Apply the most recent stash (keeps it in the stash list)
git stash apply

# Apply and remove from stash list
git stash pop

# Apply a specific stash
git stash apply stash@{2}

# Drop a specific stash
git stash drop stash@{0}

# Clear all stashes
git stash clear
```

**Common scenario:**
1. You're working on a feature
2. An urgent bug comes in
3. `git stash` your current work
4. Fix the bug on another branch
5. Come back and `git stash pop`

## git cherry-pick — Apply Specific Commits

Cherry-pick lets you copy a specific commit from one branch to another without merging the entire branch.

```bash
# Apply a specific commit to the current branch
git cherry-pick abc1234

# Cherry-pick without auto-committing (just stage the changes)
git cherry-pick --no-commit abc1234

# Cherry-pick a range of commits
git cherry-pick abc1234..def5678
```

**When to use:**
- A bugfix on `develop` that you also need on `main`
- Pulling a single feature commit without merging everything else

## reset vs revert — Undoing Changes

### `git reset` — Move HEAD backward (rewrites history)

```bash
# Soft: undo commit, keep changes staged
git reset --soft HEAD~1

# Mixed (default): undo commit, unstage changes
git reset HEAD~1

# Hard: undo commit, discard all changes (DANGEROUS)
git reset --hard HEAD~1
```

### `git revert` — Create a new commit that undoes a previous one (safe)

```bash
# Revert a specific commit
git revert abc1234

# Revert without auto-committing
git revert --no-commit abc1234
```

### When to use which?

| | `reset` | `revert` |
|---|---------|----------|
| Rewrites history | Yes | No |
| Safe for shared branches | **No** | **Yes** |
| Creates new commit | No | Yes |
| Use case | Undo local mistakes | Undo published commits |

**Rule of thumb:** Use `revert` for commits already pushed to a shared branch. Use `reset` only for local, unpushed commits.

## .gitignore — Excluding Files from Tracking

A `.gitignore` file tells Git which files to ignore. Place it in the root of your repository.

### Common patterns

```gitignore
# Compiled files
*.pyc
__pycache__/
*.class

# Dependencies
node_modules/
venv/
.env

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db

# Build output
dist/
build/
*.egg-info/
```

### Tips

```bash
# Check what's being ignored
git status --ignored

# Track a file that's currently ignored (force add)
git add -f secret-but-needed.env

# Remove a file from tracking but keep it locally
git rm --cached file-to-untrack.txt
```

See [.gitignore-example](.gitignore-example) for templates.

## Other Useful Commands

### `git blame` — Who changed each line?

```bash
git blame filename.py
```

### `git bisect` — Find the commit that introduced a bug

```bash
git bisect start
git bisect bad            # Current commit is broken
git bisect good abc1234   # This commit was working
# Git will checkout commits for you to test
# Mark each as good or bad until the culprit is found
git bisect reset          # When done
```

### `git clean` — Remove untracked files

```bash
# Dry run (preview what will be deleted)
git clean -n

# Delete untracked files
git clean -f

# Delete untracked files and directories
git clean -fd
```

