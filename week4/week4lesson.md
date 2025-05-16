# Week 4 - Working with Files, APIs, and JSON

## Learning Objectives
By the end of this week, students will:
- Read from and write to files in Python.
- Handle data stored in JSON format.
- Fetch and process data from web APIs.
- Apply CLI utilities to inspect files and data.
- Continue practicing Git workflow for iterative development.

---

## Day 1 - File Input and Output

### Topics
- Reading Files with `open()` and `.read()`
  - Example:
    ```python
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
    ```

- Writing to Files with `.write()`
  - Example:
    ```python
    with open("output.txt", "w") as file:
        file.write("Hello, file!")
    ```

- Appending to Files with `"a"` mode
- CLI Commands for Inspecting Files:
  - `cat`, `head`, `tail`, `grep`

- Quiz and Homework Review

### Day 1 Homework
1. Write a script that asks the user for a list of tasks and writes them to `tasks.txt`.
2. Write another script that reads and prints the contents of `tasks.txt`.

### Day 1 Quiz (Sample Questions)
1. How do you open a file named `notes.txt` for reading in Python?
2. What is the CLI command to print the first 10 lines of a file?
3. What file mode would you use to add content without overwriting existing data?

---

## Day 2 - JSON Handling and API Requests

### Topics
- Introduction to JSON
  - Example JSON structure:
    ```json
    {"name": "Alice", "age": 30}
    ```

- Reading JSON in Python
  - Example:
    ```python
    import json

    with open("data.json", "r") as file:
        data = json.load(file)
        print(data["name"])
    ```

- Writing JSON in Python
  - Example:
    ```python
    with open("output.json", "w") as file:
        json.dump({"status": "complete"}, file)
    ```

- Making API Requests with `requests`
  - Example:
    ```python
    import requests

    response = requests.get("https://api.github.com")
    print(response.json())
    ```

- Quiz and Homework Review

### Day 2 Homework
1. Write a script that fetches a random joke from the `https://official-joke-api.appspot.com/random_joke` API and prints the setup and punchline.
2. Save the joke response to a JSON file called `joke.json`.
3. Commit and push the script and the `joke.json` file to GitHub.

### Day 2 Quiz (Sample Questions)
1. Write the Python code to load JSON data from a file called `user.json`.
2. What Python module is commonly used to make HTTP requests?
3. What is the CLI command to search for the word "error" in a file named `server.log`?

---

## Bonus Session (Optional)

### Topics
- Parsing API Data with Query Parameters
  - Example:
    ```python
    import requests

    city = "London"
    api_key = "your_api_key"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    print(response.json())
    ```

- CLI Utilities for Data Inspection
  - Using `jq` to pretty-print JSON data

- Mini Project: Weather CLI App
  - Allow the user to enter a city name.
  - Fetch and display the weather information from a public API.
  - Save the response to a file.

---

## Summary
- Reading and writing files in Python
- Working with JSON data
- Fetching data from APIs using `requests`
- Using CLI utilities to explore file contents
- Applying Git to commit and manage code changes
