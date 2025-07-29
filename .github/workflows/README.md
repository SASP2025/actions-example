
# Test Workflow with Pytest

The pytest GitHub Actions workflow tests Python code using `pytest`. If `pytest-cov` is available, it also includes a coverage report.

There are "test_*" files in this directory which are used to test the actions themselves and should not be called by other repositories.

## What this workflow does

- Installs dependencies from `pyproject.toml` using the `[tests]` optional dependencies.
- Runs `pytest` with or without coverage, depending on the input.
- Logs results in the GitHub Actions Job Summary so it's easy to view.
- Can be triggered manually using the `workflow_dispatch` input for environment selection.

## Location

This file lives in:  .github/workflows

You can trigger it manually from GitHub by selecting the **Run workflow** button and choosing the environment (`production` for now).

When testing from an external repository, you'll want to call the action with specific triggers for things like pull requests.

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
- Your tests follow pytest expectations and what you've specified in your pyproject.toml file 

##  Example usage

In order to execute the pytest reusable workflow, make sure it is called as a job:

```yaml
  test-production-with-coverage:
    uses: SASP2025/actions-example/.github/workflows/reusable_pytest.yml
    with:
      coverage: true
      environment: production

  test-production-without-coverage:
    uses: SASP2025/actions-example/.github/workflows/reusable_pytest.yml
    with:
      coverage: false
      environment: production

