# Contributing

Spotted a typo, broken link, or unclear explanation? Contributions are welcome — and the workflow itself is good Git practice.

## Quick fixes (one-line edits)

If you have a GitHub account, the fastest path is to edit the file directly on GitHub:

1. Open the file in the repo.
2. Click the pencil ✏️ icon.
3. Make your change.
4. Scroll down, write a short commit message, and select **"Create a new branch and start a pull request"**.

## Larger changes (new exercises, restructuring)

1. **Fork** this repo on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/intro-to-git.git
   cd intro-to-git
   ```
3. Add this repo as `upstream` so you can pull future updates:
   ```bash
   git remote add upstream https://github.com/Rengoku02/intro-to-git.git
   ```
4. Create a feature branch:
   ```bash
   git switch -c fix/improve-section-2
   ```
5. Make and commit your changes (use imperative-mood commit messages — see [01-basics](01-basics/README.md)):
   ```bash
   git add -A
   git commit -m "Clarify rebase example in section 2"
   ```
6. Push your branch and open a Pull Request:
   ```bash
   git push -u origin fix/improve-section-2
   ```

## Style guide

- **Markdown** — fence all code blocks with the language tag (` ```bash`, ` ```python`).
- **Commit messages** — imperative mood, ≤ 50 characters on the first line.
- **Tone** — concise, beginner-friendly, with a bioinformatics example wherever it fits naturally.
- **No tracked binaries** — large files belong in LFS or external storage. The pre-commit hook in [04-workflows](04-workflows/README.md) catches accidental commits >500 kB.

## Reporting issues

Open a GitHub issue with:
- The page (and section heading) where you found the problem
- What's wrong / unclear
- A suggested fix, if you have one

Thanks for helping make this tutorial better!
