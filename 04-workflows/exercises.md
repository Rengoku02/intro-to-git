# Exercises: Workflows & Beyond

Use the `git-bio-project` repo you pushed to GitHub in Section 3.

### Exercise 1: Practice GitHub Flow

1. Create a branch: `git switch -c feature/add-reverse-complement`
2. Create a new file called `reverse_complement.py`:
   ```python
   COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}

   def reverse_complement(sequence):
       """Return the reverse complement of a DNA sequence."""
       return "".join(COMPLEMENT[base] for base in reversed(sequence.upper()))

   if __name__ == "__main__":
       seq = "ATGCGA"
       print(f"Reverse complement of {seq}: {reverse_complement(seq)}")
   ```
3. Commit and push:
   ```bash
   git add reverse_complement.py
   git commit -m "Add reverse complement function"
   git push -u origin feature/add-reverse-complement
   ```
4. Open a PR on GitHub, review the diff, and merge it
5. Pull the merged changes locally: `git pull origin main`

### Exercise 2: Tag a Release

1. Make sure you're on `main` with your latest changes
2. Create an annotated tag: `git tag -a v1.0.0 -m "First release of bio-tools"`
3. Push the tag: `git push origin v1.0.0`
4. View it on GitHub under "Releases"

### Exercise 3: Practice Stashing

1. Open any of your Python files and make a change (e.g., add a comment) — don't commit
2. Stash the changes: `git stash push -m "WIP: experimenting with output format"`
3. Verify your working directory is clean: `git status`
4. Restore the changes: `git stash pop`
5. Verify the change is back with `git diff`

### Exercise 4: Create a .gitignore

1. Create some files that a bioinformatics project would typically ignore:
   ```bash
   touch results.log alignment_output.sam large_genome.fasta.gz
   mkdir __pycache__
   touch __pycache__/module.cpython-39.pyc
   ```
2. Create a `.gitignore` file with patterns to ignore them:
   ```gitignore
   # Log files
   *.log

   # Large data files
   *.sam
   *.bam
   *.fasta.gz
   *.fastq.gz

   # Python cache
   __pycache__/
   *.pyc
   ```
3. Run `git status` — the ignored files shouldn't appear
4. Stage and commit: `git add .gitignore && git commit -m "Add .gitignore for bio project"`
