# Introduction to Git for Bioinformatics

A tutorial for learning Git.

## Why Git in Bioinformatics?

Reproducibility is a cornerstone of good science. In bioinformatics, your analysis code **is** your methods section. Git helps you:

- **Track every change** to your analysis scripts, pipelines, and parameters — so you can always reproduce a result or trace how it was generated
- **Version your workflows** — whether you're writing R scripts, Python pipelines, Snakemake/Nextflow workflows, or shell scripts for sequence processing
- **Collaborate on research** — share code with lab members via GitHub
- **Recover from mistakes** — accidentally break a working pipeline? Git lets you roll back to any previous version
- **Document your process** — commit messages serve as a lab notebook for your computational work

If you've ever had files named `analysis_v2_final_FINAL.py`, Git is the solution.

## Prerequisites

- **Git** installed on your machine ([Download Git](https://git-scm.com/downloads))
- A **GitHub account** ([Sign up](https://github.com/signup))

## Table of Contents

| # | Section | Topics |
|---|---------|--------|
| 1 | [Git Basics](01-basics/README.md) | `init`, `clone`, `add`, `commit`, `status`, `log`, `diff`, `config` |
| 2 | [Branching & Merging](02-branching/README.md) | `branch`, `switch`, `merge`, `rebase`, conflict resolution |
| 3 | [Remotes & GitHub](03-remote-and-github/README.md) | `remote`, `push`, `pull`, `fetch`, forking, pull requests |
| 4 | [Workflows & Beyond](04-workflows/README.md) | Git Flow, GitHub Flow, trunk-based, tagging, `stash`, `cherry-pick`, `reset` vs `revert`, `reflog`, Git LFS, hooks, GitHub Actions, signed commits, submodules, `.gitignore` |
| - | [Cheat Sheet](cheatsheet.md) | Quick-reference for all commands |

Each section has an `exercises.md` (try first) and a `solutions.md` (check yourself). A bioinformatics-flavored [`.gitignore-example`](.gitignore-example) lives at the repo root.

## Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The repo is MIT-licensed ([LICENSE](LICENSE)).

