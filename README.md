# Azure Function Python v2 Blueprint Template

This repository contains a template for creating an Azure Function using Python v2 and blueprints.

## Features

-   Azure Function v2 with blueprints
-   Unit testing with pytest
-   BDD testing with pytest-bdd and Gherkin
-   Automated linting, static analysis, and unit test using tox
-   Pre-commit configuration for formatting
-   DevOps pipeline to test, build and deploy
-   Devcontainer configuration for development

## Requirements

-   Azure Functions Core Tools v2.x or later
-   Python 3.9 or later
-   Visual Studio Code with the Remote - Containers extension installed
-   Optionally if not running in Devcontainer
    - Pipenv installed
    - Pre-commit installed

## Getting Started

1.  Clone the repository
2.  Open the repository in Visual Studio Code
3.  When prompted, reopen the repository in a Devcontainer
4.  In the Devcontainer terminal, run the command `pipenv install --dev` to install the required dependencies
5.  Start Pipenv shell `pipenv shell` or run commands with `pipenv run` 
6.  To run the function locally, run the command `func start`
7.  To run the unit tests and BDD tests, run the command `pytest` or `tox -e pytest`
8.  To run the linter and static analysis, as well as tests, run the command `tox`
9.  To format the code according to pre-commit configuration, run the command `pre-commit run --all-files`
10. To build and deploy the function, configure the DevOps pipeline to suit your needs.

## Pre-commit

This template uses the  [pre-commit](https://pre-commit.com/) tool to enforce code formatting and consistency. Pre-commit is a framework for managing and maintaining multi-language pre-commit hooks.

The pre-commit configuration for this template can be found in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file. The configuration specifies which hooks should be run, in what order, and with what arguments.

To install the pre-commit hooks, run the command `pre-commit install`. After installation, the hooks will run automatically before every commit. If a hook fails, the commit will be aborted, allowing you to fix any issues before committing the changes.

## Pytest, Unit Testing, and BDD

This template includes the [pytest](https://pytest.org/) testing framework, which is used for both unit testing and behavior-driven development (BDD) testing.

Unit tests can be written in the `tests/unit_tests` directory and BDD tests can be written in the `tests/bdd` directory. BDD tests use the [pytest-bdd](https://pypi.org/project/pytest-bdd/) plugin and are written in the Gherkin language.

To run both tests, use the command `pytest`. To select which tests to run, use `pytest <folder>`. 

Both unit tests and BDD tests are automatically run in the DevOps pipeline's build stage, ensuring that any changes to the code do not introduce regressions or unexpected behavior.

## Tox

This template uses [tox](https://tox.readthedocs.io/en/latest/) to automate linting, static analysis, and unit testing. Tox is a generic virtualenv management and test command line tool that can be used for checking and maintaining different Python environments.

The tox configuration for this template can be found in the [tox.ini](tox.ini) file. The configuration specifies the different environments that should be created and the commands that should be run in each environment. In this template, tox is used to run flake8, mypy, vulture, bandit, and pytest.

-   `flake8`: is a Python library that analyzes the code's syntax and style, enforcing PEP 8 rules.
-   `mypy`: is an optional static type checker for Python that aims to combine the benefits of both dynamic (or "duck") and static typing.
-   `vulture`: is a Python library that detects unused code, making it easier to identify and remove dead code from the project.
-   `bandit`: is a Python security linter that identifies common security issues in Python code.
-   `pytest`: is a testing framework that makes it easy to write small tests, yet scales to support complex functional testing.

To run tox, simply run the command `tox` in the root directory of the project. This will run the commands specified in the `tox.ini` file in each of the specified environments.

Using tox and these libraries/tools helps ensure that the codebase is consistent, adheres to best practices, is properly tested, and is secure.

## DevOps Pipeline

The DevOps pipeline is configured using Azure Pipelines. The pipeline contains the following stages:

1.  Test - Runs unit tests in Azure Function.
2.  Build - Builds the Azure Function and runs unit tests.
3.  Deploy to Dev - Deploys the Azure Function to the development environment.

The pipeline is triggered on changes to the `main` branch.

## License

This project is licensed under the [MIT License](./LICENSE).

