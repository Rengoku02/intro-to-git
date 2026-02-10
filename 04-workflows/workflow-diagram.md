# Workflow Diagrams

## GitHub Flow

```
         main
           |
           v
    A------B------E------F
            \    /
             C--D
          (feature branch)
            + PR review
```

**Steps:**
1. Branch from `main`
2. Add commits
3. Open Pull Request
4. Discuss and review
5. Merge to `main`
6. Deploy

---

## Git Flow

```
    main      A-----------------------G--------H
               \                     / \      /
    develop     B----C----D----E----F    \    /
                      \        /         hotfix
                       X------Y
                     (feature branch)

    Legend:
    A = Initial release
    B-F = Development work
    X-Y = Feature branch
    G = Release merge to main
    H = Hotfix merged to main
```

**Branch types:**
- `main` — production-ready
- `develop` — integration branch
- `feature/*` — new features
- `release/*` — release prep
- `hotfix/*` — emergency fixes

---

## Trunk-Based Development

```
    main: ──A──B──C──D──E──F──G──H──
              |        |
         (small, frequent commits)
         (feature flags for WIP)

    Optional short-lived branches (< 1 day):

    main: ──A──B──C──────E──F──
                    \   /
                     D
                  (merged same day)
```

**Key principles:**
- Commit to main frequently
- Keep branches short-lived (hours, not days)
- Use feature flags for incomplete work
- CI runs on every commit
