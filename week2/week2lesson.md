# Week 2 - Git, GitHub, and Modular Python

## Learning Objectives
By the end of this week, students will:
- Understand the basics of Git for version control.
- Push code to GitHub.
- Organize Python code using functions and modules.
- Practice more CLI usage for Git operations.

---

## Day 1 - Git Basics and Modular Python

### Topics
- Introduction to Git
  - What is version control?
  - Git basics: `git init`, `git add`, `git commit`
  - Git config setup:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```
  - Example Workflow:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

- Introduction to GitHub
  - Creating a GitHub account
  - Creating a repository
  - Connecting local Git to GitHub:
    ```bash
    git remote add origin <repository-url>
    git push -u origin main
    ```

- Python Functions and Imports
  - Defining and calling functions
  - Example:
    ```python
    def greet(name):
        print(f"Hello, {name}!")
    
    greet("Alice")
    ```

  - Organizing functions into a separate `.py` file and importing

- Quiz and Homework Review

### Day 1 Homework
1. Create a Python file named `math_utils.py` with a function to add two numbers.
2. Create a main Python script that imports `math_utils` and uses the add function.
3. Initialize a Git repository, commit the files, and push them to GitHub.

### Day 1 Quiz (Sample Questions)
1. Write the Git commands to initialize a repo and make the first commit.
2. Write a Python function named `multiply` that takes two numbers and returns their product.
3. What is the command to push your code to GitHub?

---

## Day 2 - Error Handling, CLI Arguments, and Git Branching

### Topics
- Error Handling with `try`, `except`
  - Example:
    ```python
    try:
        number = int(input("Enter a number: "))
        print(10 / number)
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    ```

- Using CLI Arguments with `sys.argv`
  - Example:
    ```python
    import sys
    print(f"Arguments received: {sys.argv}")
    ```

- Advanced Git Usage
  - Branching:
    ```bash
    git branch new-feature
    git checkout new-feature
    ```
  - Merging:
    ```bash
    git checkout main
    git merge new-feature
    ```

- Quiz and Homework Review

### Day 2 Homework
1. Write a Python script that accepts a number from CLI arguments and prints its square.
2. Create a new Git branch called `feature-square`.
3. Add, commit, and merge the branch into `main`.
4. Push the updated `main` branch to GitHub.

### Day 2 Quiz (Sample Questions)
1. Write a Python `try/except` block that handles division by zero.
2. What command creates and switches to a new Git branch called `feature-login`?
3. How do you access the first CLI argument passed to a Python script?

---

## Bonus Session (Optional)

### Topics
- GitHub SSH Key Setup
  - Generate SSH key:
    ```bash
    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```
  - Add SSH key to GitHub

- GitHub Pull Requests Basics
  - Forking repositories
  - Creating pull requests

- Mini Project: Modular To-Do List Manager
  - Create a `todo_utils.py` file with functions to:
    - Add tasks
    - List tasks
    - Remove tasks
  - Build a `main.py` to interact with these utilities.

---

## Summary
- Git and GitHub basics
- Creating and using Python modules
- CLI argument handling
- Error handling with `try/except`
- Branching and merging with Git
