# practicePython

A small Python practice repository containing algorithm experiments, object-oriented examples, decorators, string/list manipulation snippets, and a minimal pytest-based test setup.

## Project Overview

This repository is a collection of Python exercises and learning examples rather than a packaged application. It includes:

- Basic Python syntax and list/tuple manipulation
- Sorting, deduplication, and counting examples
- Object-oriented programming examples with inheritance
- A simple decorator demonstration
- Regular expression usage
- Pytest fixtures and basic assertions
- CI configuration for GitHub Actions and Jenkins

Some files appear to be exploratory scratch code and may contain commented-out sections or incomplete experiments.

## Setup Instructions

### Prerequisites

- Python 3.11+ recommended
- `pip`
- Optional: `pytest` for running tests locally

### Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Run tests

```bash
pytest
```

## Usage Examples

### Run the practice scripts

The repository contains standalone Python files that can be executed directly for experimentation:

```bash
python pyexpr.py
python codes.py
```

Note: `pyexpr.py` prints several example outputs when run, and `codes.py` appears to be an in-progress scratch file with incomplete code fragments.

### Run the test suite

```bash
pytest
```

The included tests demonstrate basic fixture usage and assertions:

- validating a sample user dictionary
- checking list contents with fixtures

## File Structure

```text
practicePython/
├── .github/workflows/ci.yml   # GitHub Actions workflow for install + pytest
├── Jenkinsfile                # Jenkins pipeline definition
├── codes.py                   # Practice snippets and exploratory code
├── conftest.py                # Pytest configuration/fixtures (if any)
├── pyexpr.py                  # Main practice script with Python examples
├── requirements.txt           # Python dependency list
└── test_pytest_expr.py        # Pytest test cases
```

## Additional Notes

- `requirements.txt` currently pins only `pytest==9.0.2`.
- GitHub Actions is configured to run tests on push and pull requests targeting `main`.
- The Jenkins pipeline also installs dependencies and runs `pytest`.
- `conftest.py` is present in the repo, but no content was visible in the indexed view; if it contains fixtures locally, they will be auto-discovered by pytest.
- Some examples in `pyexpr.py` and `codes.py` are educational and print output directly rather than exposing reusable functions.

## Contributing

If you want to expand the repo, consider:

- Moving reusable examples into importable modules
- Splitting scripts by topic (strings, lists, OOP, regex, etc.)
- Adding docstrings and comments for each exercise
- Expanding the pytest suite with more cases
