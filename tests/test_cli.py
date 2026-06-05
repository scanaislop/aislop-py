from __future__ import annotations

import unittest
from unittest import mock

from aislop_py import cli


class CommandTest(unittest.TestCase):
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
                    "aislop@0.10.2",
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
                    "aislop@0.10.2",
                    "--",
                    "aislop-mcp",
                ],
            )

    def test_command_errors_when_node_tooling_is_missing(self) -> None:
        with mock.patch("shutil.which", return_value=None):
            self.assertIsNone(cli._command("aislop", []))


if __name__ == "__main__":
    unittest.main()
