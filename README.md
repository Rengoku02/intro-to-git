# Introduction to Git for Bioinformatics

A tutorial for learning Git.

## Why Git in Bioinformatics?

Reproducibility is a cornerstone of good science. In bioinformatics, your analysis code **is** your methods section. Git helps you:

- **Track every change** to your analysis scripts, pipelines, and parameters — so you can always reproduce a result or trace how it was generated
- **Version your workflows** — whether you're writing R scripts, Python pipelines, Snakemake/Nextflow workflows, or shell scripts for sequence processing
- **Collaborate on research** — share code with lab members, reviewers, and the broader community via GitHub
- **Recover from mistakes** — accidentally break a working pipeline? Git lets you roll back to any previous version
- **Document your process** — commit messages serve as a lab notebook for your computational work

If you've ever had files named `analysis_v2_final_FINAL.py`, Git is the solution.

## Prerequisites

- **Git** installed on your machine ([Download Git](https://git-scm.com/downloads))
- A **GitHub account** ([Sign up](https://github.com/signup))
- A **terminal** (Terminal on macOS/Linux, Git Bash on Windows)
- **Python 3** installed (for the exercise scripts)
- Basic comfort with the command line

## How to Use This Tutorial

1. **Read through each section** in order — each one builds on the previous
2. **Follow the exercises on your own machine** — each exercise is self-contained and walks you through creating files and repos from scratch
3. **Practice is key** — reading alone won't make Git stick. Try every exercise.

## Table of Contents

| # | Section | Topics |
|---|---------|--------|
| 1 | [Git Basics](01-basics/README.md) | `init`, `clone`, `add`, `commit`, `status`, `log`, `diff`, `config` |
| 2 | [Branching & Merging](02-branching/README.md) | `branch`, `switch`, `merge`, `rebase`, conflict resolution |
| 3 | [Remotes & GitHub](03-remote-and-github/README.md) | `remote`, `push`, `pull`, `fetch`, forking, pull requests |
| 4 | [Workflows](04-workflows/README.md) | Git Flow, GitHub Flow, trunk-based development, tagging |
| 5 | [Advanced Tips](05-advanced-tips/README.md) | `stash`, `cherry-pick`, `reflog`, `reset` vs `revert`, `.gitignore` |
| - | [Cheat Sheet](cheatsheet.md) | Quick-reference for all commands |

## Who Is This For?

Students and researchers in bioinformatics who want to use Git for reproducible, collaborative computational work.

---

*Created for the Reproducible Bioinformatics class seminar.*
