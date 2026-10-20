# Conventions

- Python 3.12. One virtualenv at the repo root (`.venv`); dependencies go in `pyproject.toml`.
- Format and lint with `ruff` (`ruff format .`, `ruff check .`). Line length 100.
- Tests use `pytest`. Put shared tests in `tests/`, project tests in `<project>/tests/`.
- CI (GitHub Actions) runs `ruff` and `pytest` on every push; keep it green.
- **Never commit secrets.** Keys live in `.env` (gitignored); add every new variable to `.env.example` with an empty value.
- Never commit data files or model artifacts; they're gitignored. Document how to fetch or rebuild them instead.
- Each project folder (`01-pulse/` … `05-atlas/`) is self-contained, with its own README.
- Record decisions in `docs/` and add an entry to `docs/weekly-log.md` each week.
