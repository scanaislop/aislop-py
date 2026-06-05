from __future__ import annotations

import os
import shutil
import sys

NPM_PACKAGE = os.environ.get("AISLOP_NPM_PACKAGE", "aislop@0.10.2")


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
        print(
            "aislop requires Node.js with npm/npx available on PATH.", file=sys.stderr
        )
        return 127

    os.execv(command[0], command)
    return 127


def main() -> int:
    return _run("aislop")


def main_mcp() -> int:
    return _run("aislop-mcp")


if __name__ == "__main__":
    raise SystemExit(main())
