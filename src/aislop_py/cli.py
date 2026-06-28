from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

from . import __version__

NPM_PACKAGE = os.environ.get("AISLOP_NPM_PACKAGE", f"aislop@{__version__}")


def _detect_install_channel() -> str:
    existing = os.environ.get("AISLOP_INSTALL_CHANNEL", "").strip().lower()
    if existing:
        return existing

    script = Path(sys.argv[0]).resolve()
    script_path = str(script).lower()

    if "pipx" in script_path or os.environ.get("PIPX_HOME"):
        return "pipx"

    if "site-packages" in script_path or "/.local/bin/" in script_path:
        return "pip"

    return "pip"


def _command(bin_name: str, argv: list[str]) -> list[str] | None:
    npx = shutil.which("npx")
    if npx:
        return [npx, "--yes", "--package", NPM_PACKAGE, bin_name, *argv]

    npm = shutil.which("npm")
    if npm:
        return [npm, "exec", "--yes", "--package", NPM_PACKAGE, "--", bin_name, *argv]

    return None


def _run(bin_name: str, argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    command = _command(bin_name, args)
    if command is None:
        print("aislop for Python requires Node.js tooling on PATH.", file=sys.stderr)
        return 127

    env = os.environ.copy()
    env.setdefault("AISLOP_INSTALL_CHANNEL", _detect_install_channel())
    os.execve(command[0], command, env)
    return 127


def main() -> int:
    return _run("aislop")


def main_mcp() -> int:
    return _run("aislop-mcp")


if __name__ == "__main__":
    raise SystemExit(main())
