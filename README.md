# TO-DO CLI: Take Control of Your Tasks (Early Stage)

## Project Overview

This project aims to develop and expand upon a command-line to-do list tool.
It leverages the powerful `typer` package for a user-friendly CLI experience.
The project implements and enhances on the to-do CLI tool from tutotrial
[Build a Command-Line To-Do App With Python and Typer](https://realpython.com/python-typer-cli/).

## Key Technologies:

* [**`typer`**](https://github.com/tiangolo/typer-cli):
    simplified CLI development
* [**Model-View-Controller Pattern (MVC)**](https://www.instagram.com/realpython/p/C4s9d2csRN0/):
    architectural pattern
* [**Named tuples**](https://realpython.com/python-namedtuple/):
    handling the to-do data
* [**json module**](https://realpython.com/python-json/):
    managing persistent data storage
* [**configparser**](https://docs.python.org/3/library/configparser.html#module-configparser):
    handle the application’s initial settings in a configuration file
* [**pathlib**](https://realpython.com/python-pathlib/):
    file system path manipulation
* [**pytest**](https://realpython.com/pytest-python-testing/):
    unit testing

## Functionality

| Command   | Argument      | Description |
| :---:     | :---:         | --- |
| init      |               | Initializes the application’s to-do database. |
| add       | DESCRIPTION   | Adds a new to-do to the database with a description. |
| list      |               | Lists all the to-dos in the database. |
| complete  | TODO_ID       | Completes a to-do by setting it as done using its ID. |
| remove    | TODO_ID       | Removes a to-do from the database using its ID. |
| clear     |               | Removes all the to-dos by clearing the database |

## Example usage

* Initializing the to-do database:

```bash
poetry run python -m to_do init --db-path ./db/
```

* Adding a simple task:

```bash
poetry run python -m to_do add 'clean shoes!'
```

* Listing all tasks

```bash
poetry run python -m to_do --verbose list-tasks
```

* Running tests

```bash
poetry run python -m pytest .\tests\
```