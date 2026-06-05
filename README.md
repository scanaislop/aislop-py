# aislop for Python

This package exposes the `aislop` command for Python and `pipx` users.

Private install:

```sh
pipx install git+ssh://git@github.com/scanaislop/aislop-py.git
aislop scan
```

Public install, once the package is published to PyPI:

```sh
pipx install aislop
aislop scan
```

The canonical CLI is the npm package at `aislop`. This Python package is a thin launcher that runs the matching npm CLI version, so Node.js and npm/npx must be available on the machine.

For a direct Node install:

```sh
npm install -g aislop
```
