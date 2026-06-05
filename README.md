# aislop for Python

Python launcher package for the `aislop` CLI.

This package is for Python and `pipx` users who want an `aislop` command from Python packaging tools. Node.js must be available on the machine.

It exposes:

- `aislop`
- `aislop-mcp`

## Install

Private install while this repo is private:

```sh
pipx install git+ssh://git@github.com/scanaislop/aislop-py.git
```

Public install after publishing to PyPI:

```sh
pipx install aislop
```

## Use

```sh
aislop scan
aislop fix
aislop ci
aislop-mcp
```

The launcher keeps the Python package small while exposing the same `aislop` commands.

## Versioning Model

The Python package version should track the CLI version. For example, `aislop==0.10.2` launches the `0.10.2` CLI.

Do not make a fixed PyPI release float to a newer CLI version automatically. A user who installs a fixed PyPI version expects that installed package to keep running the same CLI version until they upgrade it.

Users can run `aislop upgrade` to check whether a newer release is available.

## Upgrade Users

Private git install:

```sh
pipx install --force git+ssh://git@github.com/scanaislop/aislop-py.git
```

Public PyPI install:

```sh
pipx upgrade aislop
```

Users can run `aislop upgrade` at any time to check whether a newer release is available.

## Update The Launcher

Run this after a new `aislop` version is published:

```sh
scripts/update-version.sh 0.10.3
```

Then validate:

```sh
PYTHONPATH=src python3 -m unittest discover -s tests
python3 -m pip wheel . --wheel-dir dist
pipx install --force .
aislop --version
```

Commit and push:

```sh
git add pyproject.toml src/aislop_py tests
git commit -m "Update aislop launcher to 0.10.3"
git push
```

## Publish To PyPI

When ready:

1. Make sure the `aislop` PyPI name is still available.
2. Build the package:

```sh
python3 -m pip install --upgrade build twine
python3 -m build
```

3. Upload:

```sh
python3 -m twine upload dist/*
```

4. Verify from a clean environment:

```sh
pipx install aislop
aislop --version
```

## Troubleshooting

If the command exits with a Node.js tooling error, install Node.js first:

```sh
brew install node
```

If the wrong version runs, reinstall the launcher:

```sh
pipx install --force aislop
```

For private installs:

```sh
pipx install --force git+ssh://git@github.com/scanaislop/aislop-py.git
```
