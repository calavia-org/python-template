# python-template — Agent Instructions

> **MANDATORY READ**: This repository is governed by [`~/Development/Github/AGENTS.md`](../AGENTS.md) (organization-wide rules). Per-repo rules below provide project-specific details and **cannot override** organization rules.

## Project Overview

Cookiecutter-style Python project template: a small `template` package whose CLI greets a name and reports how many public GitHub repositories that user has.

## Repository Layout

```
.
├── template/            # package: cli.py entry point
├── tests/               # pytest suite (test_main.py)
├── .devcontainer/       # VS Code dev container definition
├── .github/workflows/   # release.yaml (semantic-release)
├── pyproject.toml       # Poetry project + tool config
└── poetry.lock
```

## Tech Stack

- **Language**: Python (>=3.11,<4)
- **Dependency manager**: Poetry
- **Runtime dependency**: requests
- **Tests**: pytest
- **Lint / format**: ruff (via pre-commit)

## Environment Setup

```bash
poetry install
poetry run python -m template.cli --name world
```

## Linting & Formatting

```bash
pre-commit run --all-files
```

## Testing

```bash
# Unit tests. The CLI calls api.github.com, so this needs network access.
poetry run pytest
```

## Commits & Branches

- All commits follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `perf:`, `test:`, `build:`, `ci:`).
- Branches use conventional prefixes: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/`, `test/`, `style/`, `perf/`, `ci/`, `major/`.
- Never commit directly to `main`/`master` — every change goes through a PR with squash merge only.

## CI/CD

- PR checks: `.github/workflows/pr-check-and-test.yml` calls the org reusable `calavia-org/workflows-lib/.github/workflows/pr-check-and-test.yml@v0` — the `Pre-Commit` gate plus the PR report. `run-tox`, `run-build` and `run-unit-tests` are off because the reusable unit/build jobs do not install Poetry dependencies.
- Release: `.github/workflows/release.yaml` runs semantic-release (config in `.releaserc.json`) on push to `main`, publishing a GitHub Release and tag.

## Key Commands

| Task | Command |
|------|---------|
| Install dependencies | `poetry install` |
| Run the CLI | `poetry run python -m template.cli --name world` |
| Run tests | `poetry run pytest` |
| Run linting | `pre-commit run --all-files` |

## Gotchas & Special Cases

- `tests/test_main.py` hits the live GitHub API and asserts a fixed repository count for the user `test`; it is brittle by design and therefore runs locally rather than in CI.
- In `pyproject.toml` the project name is `python-template` while `packages = [{include = "template"}]` makes the importable package `template`.
- The legacy `.flake8` and `.isort.cfg` files are retained for editor tooling; CI lints with ruff through the canonical pre-commit config.

## References

- **README.md**: usage
- **Related repos**: `calavia-org/org-standards`, `calavia-org/workflows-lib`

---

**Last Updated**: 2026-10-12
**Maintained By**: calavia-org
