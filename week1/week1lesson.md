# 🐍 Week 1 - Python Basics & CLI Foundations

## ✅ Learning Objectives
By the end of this week, students will:
- Write basic Python scripts using `input()`, `print()`, and variables.
- Navigate the terminal to run Python scripts.
- Set up and use a Python virtual environment.
- Install Python packages with `pip3`.

---

## 🗓️ Day 1 - Python Basics + CLI Navigation

### 🧑‍🏫 Topics
- **Introduction to Python & CLI**
  - What is Python?
  - What is the CLI?
  - Opening your Terminal (macOS/Linux/WSL)

- **Python Script Basics**
  - `print()`, `input()`
  - Variables and Data Types (`str`, `int`, `float`)
  - Example:
    ```python
    name = input("What is your name? ")
    age = input("How old are you? ")
    print(f"Hello {name}, next year you will be {int(age) + 1} years old.")
    ```

- **CLI Basics Practice**
  - Key Commands:
    - `ls`
    - `pwd`
    - `cd`
    - `mkdir`
    - `touch`

- **Virtual Environments**
  - Why use a virtual environment?
  - Commands:
    - `python3 -m venv venv`
    - `source venv/bin/activate`
    - `deactivate`

- **Running Python Code**
  - Running scripts with `python3 script.py`
  - Editing with `nano` or VS Code

- **Quiz and Homework Review**

### 📝 Day 1 Homework
1. **Create a CLI Folder**
   - Make a new folder named `week1`
   - Inside it, create a Python file named `greet.py`
2. **Write a Script**
   - Ask the user for name, age, and city.
   - Print a greeting:  
     `"Hello [name] from [city], you'll be [age+1] next year!"`
3. **Run the Script**
   - Activate a
