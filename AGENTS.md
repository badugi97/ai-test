# Repository Guidelines

This repository starts intentionally minimal so that each agent can add only the essentials. Treat this guide as the shared contract: align your additions with it and adjust the guide when the repository’s needs evolve.

## Project Structure & Module Organization
Keep top-level clutter low. Place runtime code in `src/` using the `src/package/module.py` pattern, tests in `tests/`, reusable assets (datasets, fixtures, sample configs) in `assets/`, and long-form notes or ADRs in `docs/`. A typical layout:
```
repo-root/
  src/<package>/...
  tests/...
  assets/
  docs/
```
Isolated experiments belong in `experiments/<name>` and should include a short `README.md` explaining purpose and status.

## Build, Test, and Development Commands
Create a virtual environment before installing dependencies: `python -m venv .venv && source .venv/bin/activate`. Install baseline tooling with `pip install -r requirements.txt`. Run `pytest` for the unit suite, `pytest -m integration` for slower end-to-end checks, and `ruff check src tests` to lint and format. Use `make fmt` and `make test` as wrappers when adding a `Makefile`; mirror their behavior in CI.

## Coding Style & Naming Conventions
Target Python 3.11 with `ruff` enforcing PEP 8 plus project rules. Indent with four spaces, prefer dataclasses over ad-hoc dicts, and keep public APIs typed. Modules and packages use `snake_case`, classes `PascalCase`, and constants `UPPER_SNAKE_CASE`. New scripts belong in `src/<package>/cli/` and must expose a `main()` entry point.

## Testing Guidelines
Every new module needs unit coverage in `tests/`. Name test files `test_<module>.py` and functions `test_<behavior>`. Favor fixtures over hard-coded paths, and store large artifacts under `assets/fixtures`. Aim for ≥90% line coverage; run `pytest --cov=src --cov-report=term-missing`. Update or add integration tests whenever behavior crosses module boundaries.

## Commit & Pull Request Guidelines
Write commits in the imperative mood following `type(scope): summary`, e.g., `feat(api): add pricing endpoint`. Bundle related changes; avoid multi-purpose commits. Pull requests should include a concise summary, testing notes (commands run and results), linked issue numbers, and screenshots or CLI captures when behavior changes. Keep PRs small (<400 lines diff) so other agents can review quickly.
