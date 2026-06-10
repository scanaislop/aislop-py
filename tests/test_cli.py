from __future__ import annotations

import ast
from pathlib import Path
import unittest
from unittest import mock

import aislop_py
from aislop_py import cli

PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXPECTED_NPM_PACKAGE = f"aislop@{aislop_py.__version__}"


def _pyproject_version() -> str:
    for line in (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8").splitlines():
        if line.startswith("version = "):
            return ast.literal_eval(line.split("=", 1)[1].strip())
    raise AssertionError("pyproject.toml does not declare a project version")


class CommandTest(unittest.TestCase):
    def test_package_version_matches_pyproject(self) -> None:
        self.assertEqual(aislop_py.__version__, _pyproject_version())

    def test_default_npm_package_uses_python_package_version(self) -> None:
        self.assertEqual(cli.NPM_PACKAGE, EXPECTED_NPM_PACKAGE)

    def test_command_prefers_npx(self) -> None:
        with mock.patch(
            "shutil.which",
            side_effect=lambda name: f"/bin/{name}" if name == "npx" else None,
        ):
            self.assertEqual(
                cli._command("aislop", ["--version"]),
                [
                    "/bin/npx",
                    "--yes",
                    "--package",
                    EXPECTED_NPM_PACKAGE,
                    "aislop",
                    "--version",
                ],
            )

    def test_command_falls_back_to_npm_exec(self) -> None:
        with mock.patch(
            "shutil.which",
            side_effect=lambda name: f"/bin/{name}" if name == "npm" else None,
        ):
            self.assertEqual(
                cli._command("aislop-mcp", []),
                [
                    "/bin/npm",
                    "exec",
                    "--yes",
                    "--package",
                    EXPECTED_NPM_PACKAGE,
                    "--",
                    "aislop-mcp",
                ],
            )

    def test_command_errors_when_node_tooling_is_missing(self) -> None:
        with mock.patch("shutil.which", return_value=None):
            self.assertIsNone(cli._command("aislop", []))


if __name__ == "__main__":
    unittest.main()
