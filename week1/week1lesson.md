# Week 1 - Python Basics & CLI Foundations

## Learning Objectives
By the end of this week, students will:
- Write basic Python scripts using `input()`, `print()`, and variables.
- Navigate the terminal to run Python scripts.
- Set up and use a Python virtual environment.
- Install Python packages with `pip3`.

---

## Day 1 - Python Basics + CLI Navigation

### Topics
- Introduction to Python and CLI
  - What is Python?
  - What is the CLI?
  - Opening your Terminal (macOS/Linux/WSL)

- Python Script Basics
  - `print()`, `input()`
  - Variables and Data Types (`str`, `int`, `float`)
  - Example:
    ```python
    name = input("What is your name? ")
    age = input("How old are you? ")
    print(f"Hello {name}, next year you will be {int(age) + 1} years old.")
    ```

- CLI Basics Practice
  - Key Commands:
    - `ls`
    - `pwd`
    - `cd`
    - `mkdir`
    - `touch`

- Virtual Environments
  - Why use a virtual environment?
  - Commands:
    - `python3 -m venv venv`
    - `source venv/bin/activate`
    - `deactivate`

- Running Python Code
  - Running scripts with `python3 script.py`
  - Editing with `nano` or VS Code

- Quiz and Homework Review

### Day 1 Homework
1. Create a CLI Folder
   - Make a new folder named `week1`
   - Inside it, create a Python file named `greet.py`
2. Write a Script
   - Ask the user for name, age, and city.
   - Print a greeting:  
     "Hello [name] from [city], you'll be [age+1] next year!"
3. Run the Script
   - Activate a virtual environment.
   - Run the script using `python3`.

### Day 1 Quiz (Sample Questions)
1. Write the CLI command to create a folder named `projects`.
2. What does `source venv/bin/activate` do?
3. Write a Python snippet to print "Hello, Python World!".
4. What is the CLI command to list files in the current directory?

---

## Day 2 - Conditionals, Loops, and Pip

### Topics
- Review and Q&A
  - Review Homework and Quiz Results

- Conditionals in Python
  - `if`, `elif`, `else`
  - Comparison operators (`==`, `>`, `<`, `!=`)
  - Example:
    ```python
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    ```

- Loops in Python
  - `for` loops
  - `while` loops
  - Example:
    ```python
    for i in range(1, 6):
        print(i)
    ```

- Using pip and Installing Packages
  - `pip3 install requests`
  - `pip3 list`

- Error Debugging
  - Syntax and runtime error handling
  - Reading traceback messages

- Quiz and Homework Review

### Day 2 Homework
1. Build a Number Checker
   - Ask user for a number.
   - Print if it's even or odd.
   - If the number is negative, print an error message.
2. Install Requests Package
   - Run `pip3 install requests`
   - Confirm with `pip3 list`

### Day 2 Quiz (Sample Questions)
1. Write a Python `for` loop that prints numbers 1 through 5.
2. How do you install the `requests` package?
3. Write a Python conditional that checks if a variable `x` is greater than 10.

---

## Bonus Session (Optional)

### Topics
- CLI Tools Deep Dive
  - `cat`
  - `nano`
  - `head`
  - `tail`
  - `grep`

- Mini Project: Simple Number Game
  - User guesses a random number between 1 and 10.
  - Provide feedback if too high or too low.

- GitHub Account Setup
  - Create a GitHub account
  - Install Git:
    - `brew install git`
  - Set up Git config:
    ```bash
    git config --global user.name "Your Name"
    git config --global user.email "you@example.com"
    ```

---

## Summary
- Basic Python scripting
- CLI navigation
- Virtual environments
- pip package management
- Homework and Quizzes
