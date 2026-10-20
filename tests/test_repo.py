from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_env_file_is_gitignored():
    ignored = (ROOT / ".gitignore").read_text().splitlines()
    assert ".env" in ignored


def test_project_folders_exist():
    for name in ["01-pulse", "02-pulse-service", "03-carescribe", "04-resolve", "05-atlas"]:
        assert (ROOT / name).is_dir(), name
