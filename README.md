# :car: Tire Pressure Kata :car:

[![Python](https://img.shields.io/badge/Python-3.12+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Resources

These instructions where extracted from Emily Bache repository. The link to the original repository can be found in the link bellow.

[![Web](https://img.shields.io/badge/GitHub-emilybache-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/emilybache/Racing-Car-Katas)

## Description

This kata is part of the Racing Kart Kata series, which is a set of exercises to practice TDD and SOLID principles.

The idea of the kata is to write the unit tests for the Alarm class. 
The Alarm class is designed to monitor tire pressure and set an alarm if the pressure falls outside of the expected range. 
The Sensor class provided for the exercise fakes the behaviour of a real tire sensor, providing random but realistic values.

As a first step, try to get some kind of test in place before you change the class at all. If the tests are hard to write, is that because 
of the problems with SOLID principles?

When you have some kind of test to lean on, refactor the code and make it testable. Take care when refactoring not to alter the functionality, 
or change interfaces which other client code may rely on. Add more tests to cover the functionality of the particular class you've been asked to get under test.

In summary, the steps to follow are:

- First write a security network for the existing code
- Identify what SOLID principle is not being followed
- Refactor the code to make it testable and maintainable

## Objective

The objective of the kata is to identify the SOLID principle that is not being followed and refactor the code to make it testable and maintainable.

We will learn how to work with legacy code that is difficult to test and learn how to refactor step by step. We can use Mocks, Stubs or none at all to test the code.

## Configuration

The project can be configured with `poetry` and `pyenv`.
1. Install python version with pyenv:
    ```bash
    pyenv install 3.12.0
    ```
2. Install poetry:
    ```bash
    pip install poetry
    ```
3. Create a virtual environment and install dependencies:
    ```bash
    poetry install
    poetry install --dev
    ```
   
    By default, it will create the virtual environment outside the project. To create it inside, use the following command:
    ```bash
    poetry config virtualenvs.in-project true
    poetry install
    ```
4. Activate the virtual environment:
   ```bash
    poetry shell
    ```
   You can activate it manually running `source .venv/bin/activate` on Unix systems or `source .venv/Scripts/activate` on Windows.

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
poetry run pytest
```

## Learnings

1. The Open/Closed principle was not being followed. It would be difficult to add new types of alarms without modifying the Alarm class.
2. It was difficult to test the Alarm class because it was tightly coupled to the Sensor class.
3. We've learned how to use Stubs and Mocks to test a class without depending on other classes.

### Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/code-katas)


