# PySpark CI Project

## Overview

This project demonstrates how to test a PySpark data processing function automatically using **pytest** and **GitHub Actions**.

The project applies basic data cleaning rules and calculates the amount including tax. It also uses a CI workflow to run automated tests when changes are pushed or a Pull Request is opened or updated.

## Project Objectives

- Build a simple PySpark data cleaning function.
- Write automated unit tests using pytest.
- Manage project dependencies using `requirements.txt`.
- Configure GitHub Actions to run tests automatically.
- Practice Git branches, commits, pushes, Pull Requests, and merging.

## Project Structure

```text
PySpark-CI-Project/
│
├── pyspark_job.py
├── test_pyspark_job.py
├── requirements.txt
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## How It Works

### 1. Data Processing

The `clean_data()` function in `pyspark_job.py` applies the following transformations:

- Removes rows where `amount` is less than or equal to zero.
- Removes rows where `name` is NULL.
- Creates a new column called `amount_with_tax` by multiplying `amount` by `1.20`.

### 2. Automated Testing

The `test_pyspark_job.py` file contains four tests to verify that:

1. Valid records are kept.
2. Invalid amounts are removed.
3. Records with NULL names are removed.
4. The amount including tax is calculated correctly.

### 3. Continuous Integration (CI)

The GitHub Actions workflow is defined in `.github/workflows/ci.yml`.

It runs on Ubuntu and performs these steps:

1. Checks out the repository.
2. Sets up Java 17.
3. Sets up Python 3.11.
4. Installs the required dependencies.
5. Runs the tests using `pytest -v`.

The workflow is configured to run on pushes to the specified branches and when a Pull Request targeting `main` is opened, updated, or reopened.

## Technologies Used

- Python
- Apache PySpark
- pytest
- Git and GitHub
- GitHub Actions
- Java

## How to Run the Tests Locally

### Prerequisites

- A compatible Python version.
- Java installed and configured.
- The required Python packages.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Tests

```bash
pytest -v
```

**Note:** PySpark compatibility can depend on the Python and Java versions and the operating system. The CI environment uses Python 3.11 and Java 17.

## Git and GitHub Workflow

This project also provided practice with a basic Git collaboration workflow:

1. Create and track project files.
2. Stage changes using `git add`.
3. Record changes using `git commit`.
4. Upload commits using `git push`.
5. Create a feature branch.
6. Open a Pull Request targeting `main`.
7. Review automated checks in GitHub Actions.
8. Merge the Pull Request after the checks pass.

## What I Learned

- The difference between Git and GitHub.
- How the working directory, staging area, and commits work together.
- How to use branches to separate development work.
- How Pull Requests and merges help manage code changes.
- How to write basic automated tests for a PySpark function.
- How to configure a CI pipeline using GitHub Actions.
- How automated testing helps detect problems before changes are merged.

## Future Improvements

- Add more test cases for edge cases and invalid inputs.
- Improve error handling and data validation.
- Add code quality checks to the CI workflow.
- Expand the project with more PySpark transformations.
