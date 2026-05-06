# Solutions: Branching & Merging

## Exercise 1 — Basic branching

After `git merge add-rna-support`, the log graph looks like:

```bash
$ git log --oneline --graph
*   8a9b0c1 Merge branch 'add-rna-support'
|\
| * 4d5e6f7 Add RNA to DNA conversion
|/
* 2b3c4d5 Add GC content calculator
* 0fe1d2c Add filtered sequence counting
* 9d8e7f6 Update usage message
* 1a2b3c4 Add FASTA sequence counter
```

If your `main` had no other commits since branching off, Git does a **fast-forward merge** instead and there's no merge commit — the line just becomes:

```
* 4d5e6f7 Add RNA to DNA conversion
* 2b3c4d5 Add GC content calculator
```

Both outcomes are correct.

**Final `gc_content.py`:**

```python
def gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return gc / len(sequence) if len(sequence) > 0 else 0.0

def rna_to_dna(sequence):
    """Convert an RNA sequence to DNA by replacing U with T."""
    return sequence.upper().replace("U", "T")

if __name__ == "__main__":
    test_seq = "ATGCGATCGATCG"
    print(f"GC content of {test_seq}: {gc_content(test_seq):.2%}")
```

## Exercise 2 — Resolve a conflict

When the merge fails, `git status` shows:

```
both modified:   gc_content.py
```

Open the file — you'll see conflict markers around the `gc_content` return statement. Pick **one** version (or combine), delete every `<<<<<<<`, `=======`, and `>>>>>>>` line, then:

```bash
git add gc_content.py
git commit -m "Resolve GC content return format conflict"
```

A reasonable combined resolution: keep the rounded fraction (matches the `:.2%` formatter in the test print).

```python
return round(gc / len(sequence), 4) if len(sequence) > 0 else 0.0
```

If you want to bail out instead of resolving, `git merge --abort` returns you to the pre-merge state.

## Exercise 3 — Rebase

After `git rebase main`, the rebase-practice branch's commits appear *on top of* main's latest commit:

```bash
$ git log --oneline --graph --all
* f1a2b3c (HEAD -> rebase-practice) Add docstring to rna_to_dna
* e4d5f6a (main) Update test sequence in gc_content
* 8a9b0c1 Merge branch 'add-rna-support'
| ...
```

Note the **new** commit hash on rebase-practice — the original commit was rewritten on top of main's tip, so its hash changed. That's why you should never rebase commits that have already been pushed to a shared branch.
