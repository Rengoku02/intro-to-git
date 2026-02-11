# Section 2: Branching & Merging

## Why Branches?

Branches let you work on different things **in parallel** without affecting the main codebase. Think of them as independent lines of development.

```
main:     A---B---C
               \
feature:        D---E
```

- The `main` branch stays stable
- You experiment on a `feature` branch
- When ready, you merge your work back

## Branch Commands

### Create and switch branches

```bash
# List all branches (* marks the current one)
git branch

# Create a new branch
git branch feature-login

# Switch to it
git switch feature-login
# (older syntax: git checkout feature-login)

# Create and switch in one step
git switch -c feature-login
# (older syntax: git checkout -b feature-login)
```

### Delete a branch

```bash
# Delete a merged branch
git branch -d feature-login

# Force-delete an unmerged branch
git branch -D feature-login
```

### Rename a branch

```bash
# Rename the current branch
git branch -m new-name
```

## Merging

Merging combines changes from one branch into another.

### Fast-forward merge

When the target branch has no new commits since you branched off, Git just moves the pointer forward:

```bash
git switch main
git merge feature-login
```

```
Before:   main: A---B
                     \
          feature:    C---D

After:    main: A---B---C---D
```

### Three-way merge

When both branches have new commits, Git creates a **merge commit**:


```
Before:   main: A---B---E
                     \
          feature:    C---D

After:    main: A---B---E---F (merge commit)
                     \      /
          feature:    C---D
```

## Handling Merge Conflicts

Conflicts happen when two branches modify the **same lines** in the same file.

### What a conflict looks like

```
<<<<<<< HEAD
print("Hello from main branch")
=======
print("Hello from feature branch")
>>>>>>> feature-branch
```

### How to resolve

1. Open the conflicted file
2. Choose which version to keep (or combine them)
3. Remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
4. Stage and commit:
   ```bash
   git add conflicted-file.py
   git commit -m "Resolve merge conflict"
   ```

## Rebasing

Rebase replays your commits **on top of** another branch, creating a linear history:

```bash
git switch feature-login
git rebase main
```

```
Before:   main: A---B---E
                     \
          feature:    C---D

After:    main: A---B---E
                         \
          feature:        C'---D'
```

### Merge vs Rebase

| | Merge | Rebase |
|---|---|---|
| History | Preserves branch structure | Creates linear history |
| Merge commit | Yes | No |
| Safe for shared branches | Yes | **No** — never rebase shared branches |
| Best for | Integrating feature branches | Keeping feature branch up to date |

**Golden rule:** Never rebase commits that have been pushed to a shared branch.

## Exercises

### Exercise 1: Basic Branching

1. Make sure you're on `main`: `git switch main`
2. Create a new branch: `git switch -c add-farewell`
3. Open `feature-example.py` and add a `farewell()` function
4. Commit your change: `git add . && git commit -m "Add farewell function"`
5. Switch back to main: `git switch main`
6. Notice `feature-example.py` doesn't have your farewell function on `main`
7. Merge: `git merge add-farewell`
8. Check the log: `git log --oneline --graph`

### Exercise 2: Create and Resolve a Conflict

1. On `main`, edit line 3 of `feature-example.py` to say `return x + y + 1`
2. Commit: `git add . && git commit -m "Modify add on main"`
3. Create a new branch: `git switch -c conflict-branch`
4. Edit the same line 3 to say `return x + y + 100`
5. Commit: `git add . && git commit -m "Modify add on conflict-branch"`
6. Switch to main: `git switch main`
7. Try to merge: `git merge conflict-branch`
8. Resolve the conflict in your editor, then:
   ```bash
   git add feature-example.py
   git commit -m "Resolve conflict"
   ```

### Exercise 3: Try Rebasing

1. Create a branch: `git switch -c rebase-practice`
2. Make a commit on this branch
3. Switch to `main` and make a different commit
4. Switch back: `git switch rebase-practice`
5. Rebase onto main: `git rebase main`
6. Check the log: `git log --oneline --graph --all`

---

**Next:** [Section 3 — Remotes & GitHub](../03-remote-and-github/README.md)
