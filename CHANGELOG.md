# Changelog

All notable changes to the Python distribution of aislop are documented here. The CLI itself lives in the [aislop npm package](https://www.npmjs.com/package/aislop); see its changelog for scanner and rule changes.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Unreleased

## 0.18.1 (2026-10-06)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.18.1`.

Upstream 0.18.1 makes the GitHub Action run the CLI version that matches its pinned ref, shows the provider's own error when `aislop agent` fails, and patches dependency advisories. See the [CLI changelog](https://github.com/scanaislop/aislop/blob/main/CHANGELOG.md) for the detail.

## 0.18.0 (2026-10-03)

### Added

- A `.pre-commit-hooks.yaml` with a `language: python` `aislop` hook that runs `aislop scan --staged` at the pre-commit stage, for pre-commit and prek users (pre-commit 3.2.0 or later). Thanks to @pygarap.

### Changed

- Bumped the default `aislop@…` npm package pin to `0.18.0`.

Upstream 0.18.0 adds baseline mode (`aislop baseline write`, `ci.baseline`) so CI fails only on new findings. Python import checks now read every `requirements*.txt` variant, `-r` includes, and PEP 723 script metadata, and `imports.provided` lists modules the runtime supplies. aislop uses the project's own virtualenv ruff and respects ruff's `exclude` settings, and missing tools are reported instead of silently skipped. See the [CLI changelog](https://github.com/scanaislop/aislop/blob/main/CHANGELOG.md) for the detail.

## 0.17.0 (2026-10-02)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.17.0`.

Upstream 0.17.0 adds per-file `overrides` in `.aislop/config.yml`, `pi` as a provider for `aislop agent`, a hook install suggestion after a scan, and PII-free command failure telemetry. `aislop fix` now keeps exports that are still used in their own file, and dependency advisories are patched. Scores only change if you add `overrides` or the newer bundled `knip` reports differently. See the [CLI changelog](https://github.com/scanaislop/aislop/blob/main/CHANGELOG.md) for the detail.

## 0.16.1 (2026-09-09)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.16.1`.

Upstream 0.16.1 is a maintenance release: three Python rule fixes that stop `silent-recovery` and `hardcoded-url` firing where they should not, build directories pruned from scans, and dependency patches. Scores can move, since the rule fixes remove findings and the bundled lint engines were updated. See the [CLI changelog](https://github.com/scanaislop/aislop/blob/main/CHANGELOG.md) for the detail.

## 0.16.0 (2026-08-31)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.16.0`.

Upstream 0.16.0 is a scoping release: `fix` and `scan` can be limited to changed or staged files, and `fix --dry-run` previews its plan. Scores are unchanged from 0.15.0, so nothing needs re-baselining. See the [CLI changelog](https://github.com/scanaislop/aislop/blob/main/CHANGELOG.md) for the detail.

## 0.15.0 (2026-08-26)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.15.0`.

Upstream 0.15.0 is a calibration release: scores now reflect finding density rather than project size, and three rules that fired on ordinary hand-written code were corrected. **Every score moves**, most of them upward, so badges and CI thresholds need re-baselining after upgrading. See the [CLI changelog](https://github.com/scanaislop/aislop/blob/main/CHANGELOG.md) for the detail.

## 0.14.1 (2026-08-08)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.14.1`.
- Refreshed package metadata and documentation for all 10 language targets, including C# and C/C++.

## 0.14.0 (2026-07-23)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.14.0`.

## 0.13.1 (2026-06-29)

### Changed

- Bumped the default `aislop@…` npm package pin to `0.13.1`.

## 0.13.0 (2026-06-28)

### Added

- **Install channel telemetry.** The launcher sets `AISLOP_INSTALL_CHANNEL` to `pip` or `pipx` (from the script path) before delegating to the npm CLI, so PostHog can distinguish Python installs from raw `npx` traffic.

### Changed

- Bumped the default `aislop@…` npm package pin to `0.13.0`.
