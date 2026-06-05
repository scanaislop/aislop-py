# Publishing

Publishing is automated through GitHub Actions.

## Branches

- `test`: builds and publishes to TestPyPI.
- `develop`: no publish workflow runs.
- `main`: builds and publishes to PyPI.

## GitHub Secrets

Add these in GitHub:

`Settings -> Secrets and variables -> Actions -> Repository secrets`

Required secrets:

- `TEST_PYPI_API_TOKEN`: TestPyPI API token from `https://test.pypi.org/manage/account/#api-tokens`
- `PYPI_API_TOKEN`: production PyPI API token from `https://pypi.org/manage/account/#api-tokens`

Use `__token__` only when uploading manually with Twine. In GitHub Actions, store the full token value in the secret.

## First TestPyPI Publish

Add `TEST_PYPI_API_TOKEN` before creating or pushing the `test` branch for the first time.

Push or merge package changes into `test`:

```sh
git checkout -b test
git push -u origin test
```

The `Publish` workflow will build the package and upload it to TestPyPI.

Verify:

```sh
python3 -m pip install --index-url https://test.pypi.org/simple/ aislop
aislop --version
```

## Production Publish

Add `PYPI_API_TOKEN` before merging package changes into `main`.

Merge package changes into `main`. The `Publish` workflow will build the package and upload it to PyPI.

Verify:

```sh
pipx install aislop
aislop --version
```

## Version Rule

Package versions cannot be overwritten on PyPI or TestPyPI. Before publishing again, update the version:

```sh
scripts/update-version.sh 0.10.3
```

The publish workflow only runs when package files change:

- `pyproject.toml`
- `src/**`

For the first publish from an already-created branch, run the `Publish` workflow manually from GitHub and select the `test` branch.
