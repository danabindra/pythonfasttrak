## Project Structure



| Path                      | Purpose                                                         |
|--------------------------|------------------------------------------------------------------|
| `README.md`               | Course and usage documentation.                                 |
| `requirements.txt`        | List of required Python packages (e.g., `flask`).                |
| `cli_chatbot.py`          | Interactive command-line chatbot example.                       |
| `chatbot_api.py`          | Flask web API to simulate chatbot responses.                    |
| `modules/`                | Python package containing reusable conversation logic.          |
| `tests/`                  | Unit tests to validate chatbot logic.                           |
| `.gitignore`              | Prevents versioning of unnecessary files like `__pycache__/`.   |
| `setup.py`                | Python package configuration for easy installation or execution.|


* `README.md`: Project description and setup instructions.
  * `requirements.txt`: List of Python dependencies.
  * `cli_chatbot.py`: Command-line interface for the chatbot.
  * `chatbot_api.py`: API endpoints for interacting with the chatbot.
  * `modules/`: Contains the core logic and components of the chatbot.
      * `__init__.py`: Initializes the 'modules' directory as a Python package.
      * `conversation_flows.py`: Defines the logic and structure of conversation flows.
  * `tests/`: Holds the test suite for the project.
      * `test_chatbot.py`: Unit tests for the chatbot functionality.
  * `.gitignore`: Specifies intentionally untracked files that Git should ignore.
  * `setup.py`: Script for packaging and distributing the chatbot.
