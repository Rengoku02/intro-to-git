# Solutions: Workflows & Beyond

## Exercise 1 — GitHub Flow

After the merged PR + `git pull origin main`:

```bash
$ git log --oneline --graph
*   abc1234 Merge pull request #1 from YOUR-USERNAME/feature/add-reverse-complement
|\
| * def5678 Add reverse complement function
|/
* ...
```

If you select "Squash and merge" or "Rebase and merge" on the PR, the graph will be linear (no merge commit). Either is fine — pick a strategy and stick with it across the project.

**Final `reverse_complement.py`** matches the exercise verbatim. Sanity check:

```bash
$ python reverse_complement.py
Reverse complement of ATGCGA: TCGCAT
```

## Exercise 2 — Tag a release

```bash
$ git tag -a v1.0.0 -m "First release of bio-tools"
$ git push origin v1.0.0
$ git tag
v1.0.0
```

On GitHub: **Releases** → the tag appears. Click "Draft a new release" if you want to attach release notes or assets.

To **annotated** vs **lightweight**: prefer annotated (`-a`) for releases — they carry author, date, and message metadata that lightweight tags don't.

## Exercise 3 — Stashing

```bash
$ git stash push -m "WIP: experimenting with output format"
Saved working directory and index state On main: WIP: experimenting with output format

$ git status
On branch main
nothing to commit, working tree clean

$ git stash list
stash@{0}: On main: WIP: experimenting with output format

$ git stash pop
On branch main
Changes not staged for commit:
  modified:   reverse_complement.py
Dropped refs/stash@{0} (...)
```

`pop` removes the stash from the list. If you want to keep the stash around (e.g., to apply to another branch), use `git stash apply` instead.

## Exercise 4 — `.gitignore`

After committing the `.gitignore`:

```bash
$ git status
On branch main
nothing to commit, working tree clean
```

Even though `results.log`, `alignment_output.sam`, etc. exist on disk, they don't appear — confirming the patterns work. To prove it explicitly:

```bash
$ git status --ignored
Ignored files:
  alignment_output.sam
  large_genome.fasta.gz
  results.log
  __pycache__/
```

**Watchout:** `.gitignore` only affects **untracked** files. If a file is already tracked, adding its name to `.gitignore` won't stop Git from tracking changes to it. To stop tracking a file you committed by mistake:

```bash
git rm --cached unwanted.log
git commit -m "Stop tracking unwanted.log"
```

The file stays on disk but Git ignores it from now on.
