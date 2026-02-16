# Exercises

Hands-on exercises to practice Git. Each exercise is self-contained — no cloning required. You'll build a `git-bio-project` from scratch and use it throughout.

---

## Section 1: Git Basics

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

## Section 2: Branching & Merging

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

---

## Section 3: Remotes & GitHub

Use the `git-bio-project` repo you've been building in the previous sections.

### Exercise 1: Push Your Bio Project to GitHub

1. Go to GitHub and create a new repository called `git-bio-project` (don't initialize with a README)
2. In your local `git-bio-project` directory, add the remote:
   ```bash
   git remote add origin https://github.com/YOUR-USERNAME/git-bio-project.git
   ```
3. Push your code:
   ```bash
   git push -u origin main
   ```
4. Verify on GitHub that your files (`count_sequences.py`, `gc_content.py`) appear

### Exercise 2: Practice the PR Workflow

1. Create a new branch: `git switch -c add-contributors`
2. Create a `contributors.txt` file and add your name:
   ```
   # Contributors
   - Your Name
   ```
3. Commit and push:
   ```bash
   git add contributors.txt
   git commit -m "Add contributors file"
   git push -u origin add-contributors
   ```
4. Go to GitHub and click "Compare & pull request"
5. Write a title and description, then merge the PR
6. Pull the merged changes locally: `git pull origin main`

### Exercise 3: Fetch and Inspect

1. Go to your repo on GitHub and edit `contributors.txt` directly in the browser (click the pencil icon) — add a second name or a date
2. **Don't pull yet.** Instead, fetch without merging: `git fetch origin`
3. Compare what changed: `git log HEAD..origin/main --oneline`
4. When ready, merge: `git merge origin/main`
5. Verify the change is in your local file

---

## Section 4: Workflows & Beyond

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

### Exercise 4: Use the Reflog

1. Make a small commit (e.g., add a comment to any file)
2. Reset it away: `git reset --hard HEAD~1`
3. Use `git reflog` to find the lost commit's hash
4. Recover it: `git reset --hard <hash>`
5. Verify the commit is back: `git log --oneline -3`

### Exercise 5: Create a .gitignore

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

### Exercise 6: Discuss with Your Team

Consider a multi-lab genomics collaboration and discuss:
- Which workflow would fit best — GitHub Flow, Git Flow, or trunk-based? Why?
- How would you name branches for different analyses (e.g., `analysis/rnaseq-deseq2`, `pipeline/variant-calling`)?
- How often should you tag stable versions of your analysis pipelines?
