# aislop for Python

**Catch the slop AI coding agents leave in your code.**

[![PyPI version](https://img.shields.io/pypi/v/aislop.svg)](https://pypi.org/project/aislop/) [![npm downloads](https://img.shields.io/npm/dm/aislop.svg)](https://www.npmjs.com/package/aislop) [![PyPI downloads](https://img.shields.io/pepy/dt/aislop.svg?label=PyPI%20downloads)](https://pepy.tech/project/aislop) [![Homebrew tap](https://img.shields.io/badge/Homebrew-scanaislop%2Ftap-2f855a.svg)](https://github.com/scanaislop/homebrew-tap) [![GitHub stars](https://img.shields.io/github/stars/scanaislop/aislop.svg?label=GitHub%20stars)](https://github.com/scanaislop/aislop) [![CI](https://github.com/scanaislop/aislop/actions/workflows/ci.yml/badge.svg)](https://github.com/scanaislop/aislop/actions/workflows/ci.yml) [![aislop score](https://badges.scanaislop.com/score/scanaislop/aislop.svg)](https://scanaislop.com/scanaislop/aislop) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Python 3.9+](https://img.shields.io/badge/python-%3E%3D3.9-brightgreen.svg)](https://www.python.org)

The patterns Claude Code, Cursor, Codex, and OpenCode leave behind: narrative comments above self-explanatory code, swallowed exceptions, `as any` casts, hallucinated imports, duplicated helpers, dead code, todo stubs, oversized functions. Tests pass. Lint passes. The code rots anyway.

[aislop](https://github.com/scanaislop/aislop) catches them. 50+ rules across 8 language targets (TypeScript, JavaScript, Expo / React Native, Python, Go, Rust, Ruby, PHP). Scores every change 0–100. Sub-second. Deterministic — no LLM in the runtime path, same code in, same score out. MIT-licensed, free CLI.

> This package is the Python-tooling distribution of `aislop`. The CLI is identical across every channel. Prefer npm or Homebrew? See [other ways to install](#other-ways-to-install).

## Install

Use `pipx` for a global, isolated, Python-managed CLI install:

```sh
pipx install aislop
```

Then scan any project:

```sh
aislop scan
```

`pipx` keeps `aislop` in its own virtual environment, so it never collides with your project dependencies. Plain `pip install --user aislop` also works if you prefer.

## First run

From the root of a repo:

```sh
aislop scan
```

You get a single 0–100 score and a list of findings. Common next steps:

```sh
aislop fix                   # auto-fix safe issues
aislop fix -f                # aggressive fixes (deps, unused files)
aislop ci                    # CI-friendly JSON output and exit code
aislop hook install --claude # install a per-edit agent hook
aislop rules                 # see every rule
aislop doctor                # check local tool availability
```

## What gets installed

This package exposes two commands:

- `aislop` — the CLI
- `aislop-mcp` — the MCP server, for tools that speak [Model Context Protocol](#mcp-server)

## Requirements

- Python 3.9+
- `pipx` (or `pip`)
- Node.js available on `PATH` — `aislop` runs Node-based engines under the hood

On macOS:

```sh
brew install pipx node
pipx ensurepath
```

On Debian/Ubuntu:

```sh
sudo apt install pipx
pipx ensurepath
# install Node.js from https://nodejs.org or your distro's nodesource setup
```

Run `aislop doctor` to confirm every engine can run on your machine.

## Hand off to your agent

When auto-fix can't solve an issue, pass the remaining findings to your coding agent with full context:

```sh
aislop fix --claude          # Claude Code
aislop fix --codex           # Codex CLI
aislop fix --cursor          # Cursor (copies to clipboard)
aislop fix --gemini          # Gemini CLI
aislop fix --prompt          # print an agent-agnostic prompt
```

Install a hook so feedback flows back after every edit:

```sh
aislop hook install --claude # Claude Code
aislop hook install          # pick agents interactively
```

## MCP server

Expose `aislop` as MCP tools (`aislop_scan`, `aislop_fix`, `aislop_why`, `aislop_baseline`) for Claude Desktop, Cursor, or Codex:

```jsonc
{
  "mcpServers": {
    "aislop": {
      "command": "aislop-mcp"
    }
  }
}
```

## CI

```sh
aislop scan --staged              # staged files before commit
aislop ci                         # JSON output, exits 1 if score < threshold
aislop scan --sarif > aislop.sarif # SARIF 2.1.0 for GitHub code scanning
```

Set a minimum score in `.aislop/config.yml`:

```yaml
ci:
  failBelow: 70
```

More: [CI/CD docs](https://scanaislop.com/docs/ci).

## Configure

Tune rules, severities, and excluded paths in `.aislop/config.yml`:

```yaml
exclude:
  - "**/*_test.py"
  - src/generated
rules:
  ai-slop/narrative-comment: warning   # error | warning | off
```

Run `aislop init` to scaffold one. Full reference: [configuration docs](https://scanaislop.com/docs/configuration).

## Upgrade

Upgrade the Python package:

```sh
pipx upgrade aislop
```

Check whether a newer release is available:

```sh
aislop upgrade
```

## Examples

```sh
aislop scan --changes         # only changed files from HEAD
aislop scan --staged          # staged files before commit
aislop scan --sarif > aislop.sarif  # SARIF for GitHub code scanning
aislop badge                  # generate a public score badge
```

## Troubleshooting

**`aislop: command not found` after install** — run `pipx ensurepath` and reopen your shell so the `pipx` bin directory is on `PATH`.

**`Node.js not found`** — `aislop` needs Node on `PATH`. Install it (`brew install node`, or from [nodejs.org](https://nodejs.org)) and re-run `aislop doctor`.

**Command already exists** — if another install (npm or Homebrew) already owns `aislop`, pick one source. To replace it with the pipx copy: `pipx install --force aislop`.

## Other ways to install

The same CLI is also available on npm, Yarn, Bun, and Homebrew:

```sh
pipx install aislop                  # Python (this package)
npm install -g aislop                # npm
yarn global add aislop               # Yarn
bun add -g aislop                    # Bun
brew install scanaislop/tap/aislop   # Homebrew
```

See the [Homebrew tap](https://github.com/scanaislop/homebrew-tap) and the [main project README](https://github.com/scanaislop/aislop) for the npm-family options.

## For teams

[scanaislop](https://scanaislop.com) is the hosted platform for teams: PR gates with score thresholds, an org → team → project standards hierarchy, dashboards, and agent attribution. Same engines, same scores. The CLI is MIT-licensed and free.

## Links

- Main project: https://github.com/scanaislop/aislop
- Docs: https://scanaislop.com/docs
- Issues: https://github.com/scanaislop/aislop/issues
- PyPI package: https://pypi.org/project/aislop/
- Homebrew tap: https://github.com/scanaislop/homebrew-tap
