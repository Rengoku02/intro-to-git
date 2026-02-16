# Section 1: Git Basics

## What is Git?

Git is a **distributed version control system** that tracks changes to files over time. Unlike centralized systems, every developer has a full copy of the repository history on their local machine.

Key concepts:
- **Repository (repo)**: A project tracked by Git
- **Commit**: A snapshot of your files at a point in time
- **Staging area (index)**: A holding area where you prepare changes before committing
- **Working directory**: The files you see and edit on your machine

## Best Git resource
[Git Book] (https://git-scm.com/book/en/v2/)
[Git for beginners Mosh] (https://www.youtube.com/watch?v=8JJ101D3knE)
[git Tutorial(]https://www.youtube.com/watch?v=mAFoROnOfHs)


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
git clone <url> <dest>
```

This downloads the full repository (all files + history) to your machine.

### `git status` — Check the state of your files

```bash
git status
git status --short or git status -s
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
#Also works for sub directories within the current directory

#stage all the changes in the whole repo
git add --all
git add -A
```

### `git commit` — Save a snapshot

```bash
# Commit with a message
git commit -m "Add greeting function"

# Commit with a detailed message (opens your editor)
git commit

#Commit without staging
git commit -a -m "Your Message"

#If you need to revert the latest commit
git reset HEAD~
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

#show the exact code changes between each commit
git log -p

# Show last 5 commits
git log -5
```

### `.gitignore` - Ignore certain files during add/commit

```bash
#if you want some type of files to be ignored while staging and commits, create a .gitignore file and put the names in that

#can use simple regex too
echo "*.log" > .gitignore
```

**Some examples of .gitignore texts**
- ignore all .a files -> *.a
- but do track lib.a, even though you're ignoring .a files above -> !lib.a
- only ignore the TODO file in the current directory, not subdir/TODO -> /TODO
- ignore all files in any directory named build -> build/
- ignore all .pdf files in the doc/ directory and any of its subdirectories -> 
doc/**/*.pdf

### `git diff` — See what changed

```bash
# Changes in working directory (not yet staged)
git diff
```

## The Git Workflow (Modify → Stage → Commit)

Working Directory    Staging Area    Repository
      |<---git reset-----|               |
      |--- git add ----->|               |
      |                  |-- git commit->|
      |                  |               |
      |<---------- git checkout ---------|


1. **Edit** files in your working directory
2. **Stage** the changes you want to include (`git add`)
3. **Commit** the staged changes as a snapshot (`git commit`)

## Reversing changes

### `git amend` - add files to the last commit

```bash
$ git commit -m 'Initial commit'
$ git add forgotten_file
$ git commit --amend
```

### `git reset` - unstage staged files

```bash
git reset HEAD <filename>
git restore --staged <filename>
```

### `git checkout` - Unmodify modified files

```bash
git checkout -- <filename>
git restore <filename>
```
