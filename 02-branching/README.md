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

create a new one with `mkdir git-bio-project && cd git-bio-project && git init`.

### Exercise 1: Basic Branching

1. Make sure you're on `main`: `git switch main`
2. Create a new file called `gc_content.py` with this content:
   ```python
   def gc_content(sequence):
       """Calculate the GC content of a DNA sequence."""
       sequence = sequence.upper()
       gc = sequence.count("G") + sequence.count("C")
       return gc / len(sequence) if len(sequence) > 0 else 0.0

   if __name__ == "__main__":
       test_seq = "ATGCGATCGATCG"
       print(f"GC content of {test_seq}: {gc_content(test_seq):.2%}")
   ```
3. Stage and commit: `git add gc_content.py && git commit -m "Add GC content calculator"`
4. Create a new branch: `git switch -c add-rna-support`
5. Edit `gc_content.py` — add a function to handle RNA sequences:
   ```python
   def rna_to_dna(sequence):
       """Convert an RNA sequence to DNA by replacing U with T."""
       return sequence.upper().replace("U", "T")
   ```
6. Commit: `git add gc_content.py && git commit -m "Add RNA to DNA conversion"`
7. Switch back to main: `git switch main`
8. Notice `gc_content.py` doesn't have your new function on `main`
9. Merge: `git merge add-rna-support`
10. Check the log: `git log --oneline --graph`

### Exercise 2: Create and Resolve a Conflict

1. On `main`, edit the `gc_content` function to round the result:
   ```python
       return round(gc / len(sequence), 4) if len(sequence) > 0 else 0.0
   ```
2. Commit: `git add gc_content.py && git commit -m "Round GC content to 4 decimals"`
3. Create a new branch: `git switch -c conflict-branch`
4. Edit the **same line** differently — return a percentage instead:
   ```python
       return (gc / len(sequence)) * 100 if len(sequence) > 0 else 0.0
   ```
5. Commit: `git add gc_content.py && git commit -m "Return GC content as percentage"`
6. Switch to main: `git switch main`
7. Try to merge: `git merge conflict-branch`
8. You'll see a conflict! Open `gc_content.py`, resolve it by choosing one version (or combining them), remove the conflict markers, then:
   ```bash
   git add gc_content.py
   git commit -m "Resolve GC content return format conflict"
   ```

### Exercise 3: Try Rebasing

1. Create a branch: `git switch -c rebase-practice`
2. Add a comment or docstring to any function and commit
3. Switch to `main` and make a different small change (e.g., update the test sequence) and commit
4. Switch back: `git switch rebase-practice`
5. Rebase onto main: `git rebase main`
6. Check the log: `git log --oneline --graph --all`

---

**Next:** [Section 3 — Remotes & GitHub](../03-remote-and-github/README.md)
