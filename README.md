# GitHub Actions Playground

A simple Python project designed for learning GitHub Actions CI/CD workflows. This project demonstrates best practices for setting up automated testing, code coverage, and artifact management in GitHub Actions.

## 🎯 Project Overview

This project contains:
- A simple calculator module with basic arithmetic operations
- Comprehensive pytest test suite
- GitHub Actions workflow for automated testing
- Code coverage reporting

## 📁 Project Structure

```
github-actions-playground/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI/CD workflow
├── src/
│   ├── __init__.py         # Package initialization
│   └── calculator.py       # Calculator module with basic operations
├── tests/
│   ├── __init__.py         # Test package initialization
│   └── test_calculator.py  # Test suite for calculator module
├── .gitignore              # Git ignore patterns
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or 3.11
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Amit-Dvash-I/tests-private-repo.git
cd tests-private-repo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🧪 Running Tests

Run all tests:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run tests with coverage report:
```bash
pytest --cov=src --cov-report=term --cov-report=html
```

## 📊 GitHub Actions Workflow

The CI workflow (`.github/workflows/ci.yml`) demonstrates:

### ✅ Triggers
- Runs on **push** to any branch
- Runs on **pull_request** to any branch

### 🐍 Python Version Matrix
Tests run on multiple Python versions:
- Python 3.10
- Python 3.11

### ⚡ Dependency Caching
- Caches pip dependencies based on `requirements.txt`
- Speeds up subsequent workflow runs

### 📈 Code Coverage
- Generates coverage reports using `pytest-cov`
- Uploads coverage reports as artifacts
- Artifacts are retained for 30 days

### 🎁 Artifacts
Coverage reports are uploaded as artifacts and can be downloaded from the Actions tab:
- `coverage-report-3.10` - Coverage for Python 3.10
- `coverage-report-3.11` - Coverage for Python 3.11

## 📚 Learning Resources

### Key Concepts Demonstrated

1. **Workflow Triggers**: Using `on: [push, pull_request]`
2. **Matrix Strategy**: Testing across multiple Python versions
3. **Dependency Caching**: Using `cache: 'pip'` to speed up builds
4. **Test Execution**: Running pytest with coverage
5. **Artifact Upload**: Persisting test results and coverage reports

### GitHub Actions Documentation
- [GitHub Actions Quickstart](https://docs.github.com/en/actions/quickstart)
- [Workflow Syntax](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Python Testing with GitHub Actions](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

## 🛠️ Module API

### Calculator Functions

```python
from src.calculator import add, subtract, multiply, divide

# Addition
result = add(5, 3)  # Returns: 8

# Subtraction
result = subtract(10, 4)  # Returns: 6

# Multiplication
result = multiply(3, 7)  # Returns: 21

# Division
result = divide(10, 2)  # Returns: 5.0
result = divide(10, 0)  # Raises: ValueError
```

## 🤝 Contributing

Feel free to experiment with this project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push and create a pull request
5. Watch the CI workflow run!

## 📝 License

This is a learning project - feel free to use it however you like!

## 🎓 Next Steps

To extend your learning:
1. Add more complex workflows (e.g., deployment, releases)
2. Integrate code quality tools (linters, formatters)
3. Add status badges to the README
4. Experiment with different test frameworks
5. Set up coverage thresholds and requirements