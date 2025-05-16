# Python Bootcamp Bonus Track: Build a Landbot-Style Chatbot with Python

## Overview

This bonus track extends your learning by teaching you how to build a simple conversational chatbot in Python. You will implement branching logic and user interaction, similar to how no-code tools like Landbot work. You will build both:

- A **Command-Line Interface (CLI) Chatbot**  
- A **Web-Based Chatbot with Flask**

---

## Learning Outcomes

By completing this bonus track, you will:
- Model conversational flows using Python dictionaries and functions.
- Implement branching logic based on user inputs.
- Build a web chatbot API with Flask.
- Compare coded bots to no-code solutions like Landbot.

---

## CLI Chatbot Example

### Example Code

```python
def chatbot():
    print("Welcome to SimpleBot!")
    print("How can I help you today?")
    print("1. Learn about our services")
    print("2. Contact support")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        print("We offer Python training, DevOps consulting, and cloud migration services.")
    elif choice == "2":
        print("You can reach our support at support@example.com")
    else:
        print("Sorry, I didn't understand that.")
        
chatbot()
