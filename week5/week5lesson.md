# Week 5 - Virtual Environments, Testing, and Packaging

## Learning Objectives
By the end of this week, students will:
- Set up and manage Python virtual environments.
- Manage project dependencies with `pip` and `requirements.txt`.
- Write and run basic unit tests.
- Package their Python project for distribution.
- Continue working with Git and GitHub for version control.

---

## Day 1 - Virtual Environments and Dependency Management

### Topics
- Why Use Virtual Environments
- Creating a Virtual Environment
  - `python3 -m venv venv`
- Activating the Environment
  - `source venv/bin/activate`
- Deactivating the Environment
  - `deactivate`
- Managing Dependencies
  - Installing packages with `pip3 install package_name`
  - Saving dependencies to `requirements.txt`
    - `pip freeze > requirements.txt`
  - Installing from `requirements.txt`
    - `pip install -r requirements.txt`

- Quiz and Homework Review

### Day 1 Homework
1. Create a virtual environment for your project.
2. Install the `requests` and `colorama` packages.
3. Save the dependencies to `requirements.txt`.
4. Push your updated project to GitHub including `requirements.txt`.

### Day 1 Quiz (Sample Questions)
1. What is the CLI command to activate a virtual environment?
2. How do you save installed packages to `requirements.txt`?
3. Write the command to install packages listed in `requirements.txt`.

---

## Day 2 - Testing and Packaging

### Topics
- Introduction to Unit Testing
  - Writing test functions using `unittest`
    ```python
    import unittest

    def add(a, b):
        return a + b

    class TestMath(unittest.TestCase):
        def test_add(self):
            self.assertEqual(add(2, 3), 5)

    if __name__ == "__main__":
        unittest.main()
    ```
  - Running tests with `python3 -m unittest`

- Basic Debugging with Print Statements and Error Handling

- Packaging a Python Project
  - Creating `setup.py` (Basic Example)
    ```python
    from setuptools import setup

    setup(
        name='mycliapp',
        version='0.1',
        py_modules=['main'],
        install_requires=[],
    )
    ```

- GitHub Actions Overview (Optional Introduction)
  - What is Continuous Integration (CI)?
  - Overview of GitHub Actions as a CI tool

- Quiz and Homework Review

### Day 2 Homework
1. Write a unit test for one of your project functions.
2. Create a `setup.py` for your project.
3. Push your updates to GitHub with your test file and `setup.py`.

### Day 2 Quiz (Sample Questions)
1. Write a simple `unittest` that checks if `2 + 2` equals `4`.
2. What command runs all tests in Python using `unittest`?
3. What is the purpose of `setup.py`?

---

## Bonus Session (Optional)

### Topics
- GitHub Actions Workflow Example
  - Example `main.yml` for Python CI:
    ```yaml
    name: Python CI

    on: [push]

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v2
          - name: Set up Python
            uses: actions/setup-python@v2
            with:
              python-version: '3.8'
          - name: Install dependencies
            run: |
              pip install -r requirements.txt
          - name: Run tests
            run: |
              python -m unittest discover
    ```

- Mini Project: Package Your To-Do App
  - Add unit tests.
  - Create `requirements.txt` and `setup.py`.
  - Document usage in `README.md`.
  - Push final package to GitHub.

---

## Summary
- Creating and using virtual environments
- Managing dependencies with pip and requirements.txt
- Writing and running unit tests
- Packaging Python projects for distribution
- Optional introduction to GitHub Actions CI
