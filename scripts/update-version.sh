#!/usr/bin/env bash
set -euo pipefail

version="${1:?Usage: scripts/update-version.sh <version>}"

perl -0pi -e "s#version = \"[^\"]+\"#version = \"$version\"#" pyproject.toml
perl -0pi -e "s#__version__ = \"[^\"]+\"#__version__ = \"$version\"#" src/aislop_py/__init__.py

echo "Updated Python launcher to aislop $version"
