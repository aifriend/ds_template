"""Test cases for the make_dataset module."""
from pathlib import Path

from click.testing import CliRunner

from pdf2readable.data import make_dataset


def test_make_dataset_succeeds(tmp_path: Path) -> None:
    """It exits with a status code of zero for an existing input path."""
    result = CliRunner().invoke(
        make_dataset.main, [str(tmp_path), str(tmp_path / "out")]
    )
    assert result.exit_code == 0


def test_make_dataset_rejects_missing_input(tmp_path: Path) -> None:
    """It fails when the input path does not exist."""
    result = CliRunner().invoke(
        make_dataset.main, [str(tmp_path / "missing"), str(tmp_path / "out")]
    )
    assert result.exit_code != 0
