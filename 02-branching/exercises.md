# Exercises: Branching & Merging

Use the `git-bio-project` repo you created in Section 1 (or create a new one with `mkdir git-bio-project && cd git-bio-project && git init`).

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
