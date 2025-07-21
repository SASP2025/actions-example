
## EXPLANATION OF EACH SECTION OF THE ACTION FILE

#  Pytest Action for GitHub Workflows

This is a custom GitHub Action that runs your Python tests using `pytest`. It can also show code coverage results if you enable it. The action is designed to be reusable across different repositories or projects.

When you use it in your workflow, it will show the test results (and optionally coverage) directly in the GitHub Actions Job Summary.

---

##  What This Action Does

- Runs your test suite using `pytest`
- Supports optional coverage reporting using `pytest-cov`
- Outputs both test results and coverage summary in the GitHub Actions Job Summary panel

---

##  Inputs

| Input Name        | Type    | Required | Default | Description                                                 |
|-------------------|---------|----------|---------|-------------------------------------------------------------|
| `coverage`        | boolean | no       | `true`  | Whether to run pytest with code coverage                    |
| `coverage-target` | string  | no       | `"src"` | The folder or package name to check coverage for            |

>  You can change `"src"` to match the folder where your Python code lives — like `exercise_package` or `my_app`.

---

##  Example: How to Use in a Workflow

This is how your workflow file might look if you want to use this action:

```yaml
name: Run Pytest Tests

on:
  workflow_dispatch:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install test dependencies
        run: |
          python -m pip install --upgrade pip
          pip install .[tests]

      - name: Run Pytest Action
        uses: SASP2025/actions-example/.github/jobs/pytest@main
        with:
          coverage: true
          coverage-target: exercise_package


