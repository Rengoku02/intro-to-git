# Git Cheat Sheet

## Setup & Configuration

| Command | Description |
|---------|-------------|
| `git config --global user.name "Name"` | Set your name |
| `git config --global user.email "email"` | Set your email |
| `git config --global init.defaultBranch main` | Set default branch to `main` |
| `git config --list` | Show all configuration |

## Creating Repositories

| Command | Description |
|---------|-------------|
| `git init` | Initialize a new repo in the current directory |
| `git clone <url>` | Clone a remote repository |

## Basic Workflow

| Command | Description |
|---------|-------------|
| `git status` | Show changed/staged/untracked files |
| `git add <file>` | Stage a file |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit staged changes |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git log --oneline` | Compact commit history |
| `git log --oneline --graph --all` | Visual branch history |

## Branching & Merging

| Command | Description |
|---------|-------------|
| `git branch` | List branches |
| `git branch <name>` | Create a branch |
| `git switch <name>` | Switch to a branch |
| `git switch -c <name>` | Create and switch to a branch |
| `git merge <branch>` | Merge branch into current |
| `git rebase <branch>` | Rebase current onto branch |
| `git branch -d <name>` | Delete a merged branch |
| `git branch -D <name>` | Force-delete a branch |

## Remote Repositories

| Command | Description |
|---------|-------------|
| `git remote -v` | List remotes with URLs |
| `git remote add <name> <url>` | Add a remote |
| `git push -u origin <branch>` | Push and set upstream |
| `git push` | Push to upstream |
| `git pull` | Fetch and merge remote changes |
| `git pull --rebase` | Fetch and rebase |
| `git fetch` | Download remote changes without merging |

## Undoing Changes

| Command | Description |
|---------|-------------|
| `git restore <file>` | Discard working directory changes |
| `git restore --staged <file>` | Unstage a file |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged |
| `git reset HEAD~1` | Undo last commit, unstage changes |
| `git reset --hard HEAD~1` | Undo last commit, discard changes |
| `git revert <commit>` | Create a new commit that undoes a commit |

## Stashing

| Command | Description |
|---------|-------------|
| `git stash` | Stash current changes |
| `git stash push -m "message"` | Stash with a description |
| `git stash list` | List all stashes |
| `git stash pop` | Apply and remove latest stash |
| `git stash apply` | Apply latest stash (keep in list) |
| `git stash drop stash@{n}` | Delete a specific stash |

## Tags & Releases

| Command | Description |
|---------|-------------|
| `git tag` | List all tags |
| `git tag -a v1.0.0 -m "msg"` | Create an annotated tag |
| `git push origin v1.0.0` | Push a tag to remote |
| `git push origin --tags` | Push all tags |

## Inspection & Debugging

| Command | Description |
|---------|-------------|
| `git blame <file>` | Show who changed each line |
| `git bisect start` | Start binary search for a bug |
| `git cherry-pick <commit>` | Apply a specific commit |
| `git clean -n` | Preview untracked files to delete |
| `git clean -fd` | Delete untracked files and directories |

## .gitignore Patterns

| Pattern | Matches |
|---------|---------|
| `*.log` | All `.log` files |
| `build/` | The `build` directory |
| `!important.log` | Exception — track this file |
| `**/temp` | `temp` in any subdirectory |
| `doc/*.txt` | `.txt` files in `doc/` only |
