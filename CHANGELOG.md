# Changelog

All notable changes to the Python distribution of aislop are documented here. The CLI itself lives in the [aislop npm package](https://www.npmjs.com/package/aislop); see its changelog for scanner and rule changes.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## Unreleased

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
