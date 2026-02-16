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
git add analysis.py

# Stage all changes in the current directory
git add .

# Stage parts of a file interactively
git add -p analysis.py
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

### Exercise 1: Create a Bio Project and Make Your First Commits

1. Create a new project directory and initialize a Git repo:
   ```bash
   mkdir git-bio-project
   cd git-bio-project
   git init
   ```
2. Create a file called `count_sequences.py` with the following content:
   ```python
   def count_sequences(fasta_file):
       """Count the number of sequences in a FASTA file."""
       count = 0
       with open(fasta_file) as f:
           for line in f:
               if line.startswith(">"):
                   count += 1
       return count

   if __name__ == "__main__":
       print("Sequence counter ready.")
   ```
3. Check the state: `git status` — the file should appear as "untracked"
4. Stage it: `git add count_sequences.py`
5. Commit it: `git commit -m "Add FASTA sequence counter"`
6. Now modify `count_sequences.py` — change the print statement to:
   ```python
       print(f"Usage: count_sequences('sequences.fasta')")
   ```
7. Run `git status` — notice the file is now "modified"
8. Stage and commit: `git add count_sequences.py && git commit -m "Update usage message"`
9. Check the log: `git log --oneline`

### Exercise 2: Explore the Diff

1. Open `count_sequences.py` and add a new function:
   ```python
   def count_sequences_by_id(fasta_file, identifier):
       """Count sequences matching a specific identifier prefix."""
       count = 0
       with open(fasta_file) as f:
           for line in f:
               if line.startswith(">") and identifier in line:
                   count += 1
       return count
   ```
2. Before staging, run `git diff` to see your changes highlighted
3. Stage the file: `git add count_sequences.py`
4. Run `git diff --staged` to see what will be committed
5. Commit: `git commit -m "Add filtered sequence counting"`

### Exercise 3: Undo Unstaged Changes

1. Make an edit to `count_sequences.py` (e.g., delete a function)
2. Decide you don't want the change
3. Discard it: `git restore count_sequences.py`
4. Verify the file is back to its last committed state with `git diff`

---

**Next:** [Section 2 — Branching & Merging](../02-branching/README.md)
