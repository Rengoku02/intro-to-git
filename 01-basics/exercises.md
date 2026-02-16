# Exercises: Git Basics

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
