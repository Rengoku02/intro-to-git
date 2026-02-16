# Section 5: Advanced Tips

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

## git reflog — Your Safety Net

Reflog records every time HEAD moves — even actions that `git log` doesn't show (like resets, rebases, and amended commits). It's your undo history.

```bash
# View the reflog
git reflog

# Example output:
# abc1234 HEAD@{0}: commit: Add new feature
# def5678 HEAD@{1}: checkout: moving from main to feature
# ghi9012 HEAD@{2}: reset: moving to HEAD~1

# Recover a "lost" commit
git checkout abc1234

# Or reset to a previous state
git reset --hard HEAD@{2}
```

**Reflog is a lifesaver when:**
- You accidentally deleted a branch
- A rebase went wrong
- You used `reset --hard` and want to undo it

Note: Reflog entries expire after 90 days by default.

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

## Exercises

Use the `git-bio-project` repo from the previous sections.

### Exercise 1: Practice Stashing

1. Open any of your Python files and make a change (e.g., add a comment) — don't commit
2. Stash the changes: `git stash push -m "WIP: experimenting with output format"`
3. Verify your working directory is clean: `git status`
4. Restore the changes: `git stash pop`
5. Verify the change is back with `git diff`

### Exercise 2: Use the Reflog

1. Make a small commit (e.g., add a comment to any file)
2. Reset it away: `git reset --hard HEAD~1`
3. Use `git reflog` to find the lost commit's hash
4. Recover it: `git reset --hard <hash>`
5. Verify the commit is back: `git log --oneline -3`

### Exercise 3: Create a .gitignore

1. Create some files that a bioinformatics project would typically ignore:
   ```bash
   touch results.log alignment_output.sam large_genome.fasta.gz
   mkdir __pycache__
   touch __pycache__/module.cpython-39.pyc
   ```
2. Create a `.gitignore` file with patterns to ignore them:
   ```gitignore
   # Log files
   *.log

   # Large data files
   *.sam
   *.bam
   *.fasta.gz
   *.fastq.gz

   # Python cache
   __pycache__/
   *.pyc
   ```
3. Run `git status` — the ignored files shouldn't appear
4. Stage and commit: `git add .gitignore && git commit -m "Add .gitignore for bio project"`

---

**Back to:** [Main README](../README.md) | **Quick Reference:** [Cheat Sheet](../cheatsheet.md)
