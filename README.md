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
5.  To run the function locally, run the command `func start`
6.  To run the unit tests and BDD tests, run the command `pytest` or `tox -e pytest`
7.  To run the linter and static analysis, as well as tests, run the command `tox`
8.  To format the code according to pre-commit configuration, run the command `pre-commit run --all-files`
9. To build and deploy the function, configure the DevOps pipeline to suit your needs.

## DevOps Pipeline

The DevOps pipeline is configured using Azure Pipelines. The pipeline contains the following stages:

1.  Build - Builds the Azure Function and runs unit tests.
2.  Deploy to Dev - Deploys the Azure Function to the development environment.
3.  Test Dev - Runs integration tests on the Azure Function in the development environment.
4.  Deploy to Prod - Deploys the Azure Function to the production environment.
5.  Test Prod - Runs integration tests on the Azure Function in the production environment.

The pipeline is triggered on changes to the `main` branch.

## License

This project is licensed under the [MIT License](./LICENSE).



## Azure Function v2

## Testing

## Tox

## Pre-commit

## Devops pipeline
