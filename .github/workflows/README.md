
# Test Workflow with Pytest

This GitHub Actions workflow tests Python code using `pytest`. If `pytest-cov` is available, it also includes a coverage report.

## What this workflow does

- Installs dependencies from `pyproject.toml` using the `[tests]` optional dependencies.
- Runs `pytest` with or without coverage, depending on the input.
- Logs results in the GitHub Actions Job Summary so it's easy to view.
- Can be triggered manually using the `workflow_dispatch` input for environment selection.

## Location

This file lives in:  .github/workflows


You can trigger it manually from GitHub by selecting the **Run workflow** button and choosing the environment (`production` for now).

## Inputs

| Input         | Type     | Required | Default     | Description                                      |
|---------------|----------|----------|-------------|--------------------------------------------------|
| `environment` | `choice` | Yes   | `production`| Which environment to use (only `production` for now) |
| `coverage`    | `boolean`|  No    | `true`      | Whether to run pytest with code coverage         |

## Requirements

Make sure your repo is set up like this:

- Your Python package is installable (`pyproject.toml` exists and has a `[project.optional-dependencies] tests = [...]` section)
- You’ve included `pytest` and `pytest-cov` under `[project.optional-dependencies.tests]`
- Your package folder (like `my_package/`) has an `__init__.py` so it can be imported
- Your tests live in a `tests/` folder and are named like `test_*.py`

##  Example usage

Here’s how this test workflow runs two jobs:

```yaml
  test-production-with-coverage:
    uses: ./.github/workflows/test_pytest_action.yml
    with:
      coverage: true
      environment: production

  test-production-without-coverage:
    uses: ./.github/workflows/test_pytest_action.yml
    with:
      coverage: false
      environment: production

