# Solutions: Git Basics

> Try the exercises first. Use this only to check yourself.

## Exercise 1 — First commits

After step 5 (`git commit -m "Add FASTA sequence counter"`):

```bash
$ git log --oneline
1a2b3c4 Add FASTA sequence counter
```

After step 8 (`git commit -m "Update usage message"`):

```bash
$ git log --oneline
9d8e7f6 Update usage message
1a2b3c4 Add FASTA sequence counter
```

Hashes will differ on your machine — only the order and messages should match.

**Final `count_sequences.py`:**

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
    print(f"Usage: count_sequences('sequences.fasta')")
```

## Exercise 2 — Diff

`git diff` (before staging) shows your new function highlighted in green with `+` markers; the existing code is unchanged. After `git add`, `git diff` is empty (nothing unstaged), and `git diff --staged` shows the same hunk you just saw — proving that what you'll commit matches what you reviewed.

After committing, the log should read:

```bash
$ git log --oneline
0fe1d2c Add filtered sequence counting
9d8e7f6 Update usage message
1a2b3c4 Add FASTA sequence counter
```

## Exercise 3 — Discarding changes

After `git restore count_sequences.py`, `git diff` produces no output — the file matches the last commit exactly.

**Common mistake:** running `git restore --staged count_sequences.py` instead. That only un-stages; it doesn't discard working-tree changes. The plain `git restore <file>` is what reverts file contents.
