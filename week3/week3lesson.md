# Week 3 - Object-Oriented Programming (OOP) in Python

## Learning Objectives
By the end of this week, students will:
- Create and use classes to model real-world entities.
- Define methods and attributes in classes.
- Instantiate and interact with objects.
- Understand and apply basic inheritance.
- Review and manage project updates using Git.

---

## Day 1 - Introduction to Classes and Objects

### Topics
- What is Object-Oriented Programming (OOP)?
- Creating a Basic Class
  - Example:
    ```python
    class Dog:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def speak(self):
            print(f"{self.name} says woof!")

    my_dog = Dog("Buddy", "Golden Retriever")
    my_dog.speak()
    ```

- Object Instantiation and Method Calls

- Quiz and Homework Review

### Day 1 Homework
1. Create a `Car` class with attributes: `make`, `model`, `year`.
2. Add a method `display_info()` that prints these attributes.
3. Create an instance of `Car` and call the method to display its details.

### Day 1 Quiz (Sample Questions)
1. Define a class named `Book` with `title` and `author` attributes.
2. How do you create an instance of a `Person` class with name "Alice"?
3. What does `self` represent inside a class method?

---

## Day 2 - Inheritance, Method Overriding, and Git Practice

### Topics
- Inheritance Basics
  - Example:
    ```python
    class Animal:
        def speak(self):
            print("The animal makes a sound")

    class Dog(Animal):
        def speak(self):
            print("The dog barks")
    ```

- Overriding Methods
- Using `super()`

- Managing Code with Git
  - Making changes on branches
  - Committing and merging

- Quiz and Homework Review

### Day 2 Homework
1. Create a base class `Employee` with attributes: `name`, `salary`.
2. Create a subclass `Manager` that overrides a method `display_role()`.
3. Demonstrate the behavior of both classes in a `main.py` script.
4. Commit and push the updates to GitHub on a `feature-inheritance` branch.

### Day 2 Quiz (Sample Questions)
1. What is inheritance in Python? Provide a one-line definition.
2. Write a subclass `Dog` that inherits from `Animal` and overrides a `speak()` method.
3. How do you merge a branch into `main` using Git?

---

## Bonus Session (Optional)

### Topics
- Using `__str__` for Readable Object Output
  - Example:
    ```python
    class Person:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return f"Person named {self.name}"
    ```

- Adding a Simple CLI Interface to Interact with Classes
  - Example:
    ```python
    import sys
    name = sys.argv[1]
    age = sys.argv[2]
    print(f"Hello {name}, you are {age} years old.")
    ```

- Mini Project: Student and Course Management
  - Create `Student` and `Course` classes.
  - Allow adding students to a course.
  - Print course roster.

---

## Summary
- Introduction to OOP principles
- Creating and using Python classes
- Inheritance and method overriding
- Using Git to manage OOP projects
