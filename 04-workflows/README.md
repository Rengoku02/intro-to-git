# Section 4: Git Workflows

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

## Exercises

### Exercise 1: Practice GitHub Flow

1. Create a branch: `git switch -c feature/add-subtract`
2. Add a `subtract()` function to any example file
3. Commit and push: `git push -u origin feature/add-subtract`
4. Open a PR on GitHub
5. Merge the PR
6. Pull the merged changes: `git pull origin main`

### Exercise 2: Create a Tag

1. Make sure you're on `main` with your latest changes
2. Create an annotated tag: `git tag -a v1.0.0 -m "First release"`
3. Push the tag: `git push origin v1.0.0`
4. View it on GitHub under "Releases"

### Exercise 3: Discuss with Your Team

Consider your current or future projects and discuss:
- Which workflow fits best and why?
- What branch naming convention would you use?
- How often should you deploy?

---

**Next:** [Section 5 — Advanced Tips](../05-advanced-tips/README.md)
