# Solutions: Remotes & GitHub

## Exercise 1 — Push to GitHub

After `git push -u origin main`, you should see something like:

```
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
...
To https://github.com/YOUR-USERNAME/git-bio-project.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main' from 'origin'.
```

Verify the remote is wired up correctly:

```bash
$ git remote -v
origin  https://github.com/YOUR-USERNAME/git-bio-project.git (fetch)
origin  https://github.com/YOUR-USERNAME/git-bio-project.git (push)
```

**Authentication note:** GitHub no longer accepts password authentication over HTTPS. Use either a [Personal Access Token](https://github.com/settings/tokens) (when prompted for a password, paste the token) or set up SSH (see [03-remote-and-github/README.md](README.md)).

## Exercise 2 — PR workflow

After pushing, GitHub prints a banner:

```
remote: Create a pull request for 'add-contributors' on GitHub by visiting:
remote:      https://github.com/YOUR-USERNAME/git-bio-project/pull/new/add-contributors
```

Click that URL → write a clear title and description → Create pull request → Merge.

Then locally:

```bash
$ git switch main
$ git pull origin main      # fetches the merge commit GitHub created
```

Optional cleanup:

```bash
git branch -d add-contributors           # delete local branch
git push origin --delete add-contributors # delete remote branch
```

## Exercise 3 — Fetch and inspect

After editing on GitHub:

```bash
$ git fetch origin
remote: ...
From https://github.com/YOUR-USERNAME/git-bio-project
   abc1234..def5678  main -> origin/main

$ git log HEAD..origin/main --oneline
def5678 Update contributors.txt
```

`HEAD..origin/main` reads as "commits in `origin/main` but not in `HEAD`" — exactly what's incoming.

After `git merge origin/main`, the file content matches what you edited on GitHub. (If you'd rather avoid a merge commit on a fast-forward, use `git pull --ff-only` instead of `merge`.)
