# Exercises: Remotes & GitHub

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
