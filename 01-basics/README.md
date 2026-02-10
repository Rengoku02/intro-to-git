# Section 1: Git Basics

## What is Git?

Git is a **distributed version control system** that tracks changes to files over time. Unlike centralized systems, every developer has a full copy of the repository history on their local machine.

Key concepts:
- **Repository (repo)**: A project tracked by Git
- **Commit**: A snapshot of your files at a point in time
- **Staging area (index)**: A holding area where you prepare changes before committing
- **Working directory**: The files you see and edit on your machine

## Setting Up Git

Before making commits, configure your identity:

```bash
# Set your name and email (used in commit metadata)
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Check your configuration
git config --list

# Set default branch name to 'main'
git config --global init.defaultBranch main
```

## Core Commands

### `git init` — Create a new repository

```bash
mkdir my-project
cd my-project
git init
```

This creates a hidden `.git/` folder that stores all version history.

### `git clone` — Copy an existing repository

```bash
git clone https://github.com/user/repo.git
```

This downloads the full repository (all files + history) to your machine.

### `git status` — Check the state of your files

```bash
git status
```

Shows which files are:
- **Untracked**: New files Git doesn't know about
- **Modified**: Changed files not yet staged
- **Staged**: Files ready to be committed

### `git add` — Stage changes

```bash
# Stage a specific file
git add hello.py

# Stage all changes in the current directory
git add .

# Stage parts of a file interactively
git add -p hello.py
```

### `git commit` — Save a snapshot

```bash
# Commit with a message
git commit -m "Add greeting function"

# Commit with a detailed message (opens your editor)
git commit
```

**Good commit messages:**
- Use imperative mood: "Add feature" not "Added feature"
- Keep the first line under 50 characters
- Add details in the body if needed

### `git log` — View commit history

```bash
# Full log
git log

# Compact one-line view
git log --oneline

# Graphical view of branches
git log --oneline --graph --all

# Show last 5 commits
git log -5
```

### `git diff` — See what changed

```bash
# Changes in working directory (not yet staged)
git diff

# Changes that are staged (ready to commit)
git diff --staged

# Compare two commits
git diff abc123 def456
```

## The Git Workflow (Modify → Stage → Commit)

```
Working Directory    Staging Area    Repository
      |                  |               |
      |--- git add ----->|               |
      |                  |--- git commit->|
      |                  |               |
      |<---------- git checkout ---------|
```

1. **Edit** files in your working directory
2. **Stage** the changes you want to include (`git add`)
3. **Commit** the staged changes as a snapshot (`git commit`)

## Exercises

### Exercise 1: Your First Commits

1. Open `hello.py` in this folder
2. Run `git status` to see its current state
3. Modify `hello.py` — change the greeting message
4. Run `git status` again — notice the file is now "modified"
5. Stage it: `git add hello.py`
6. Commit it: `git commit -m "Update greeting message"`
7. Check the log: `git log --oneline`

### Exercise 2: Explore the Diff

1. Make another change to `hello.py` (add a new function)
2. Before staging, run `git diff` to see your changes
3. Stage the file: `git add hello.py`
4. Run `git diff --staged` to see what will be committed
5. Commit: `git commit -m "Add farewell function"`

### Exercise 3: Undo Unstaged Changes

1. Modify `hello.py` again
2. Decide you don't want the change
3. Discard it: `git checkout -- hello.py` (or `git restore hello.py`)
4. Verify the file is back to its last committed state

---

**Next:** [Section 2 — Branching & Merging](../02-branching/README.md)
