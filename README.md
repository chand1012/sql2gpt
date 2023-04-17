# SQL2GPT

SQL2GPT is a Python-based tool that extracts the schema of a SQL database and generates a prompt for ChatGPT, a large language model by OpenAI. The goal of this project is to enable users to interact with ChatGPT to generate code or ask questions related to the given database schema.

![Example](tapes/demo.gif)

## Table of Contents

* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
  + [Adding a Database Connection](#adding-a-database-connection)
  + [Printing the Schema](#printing-the-schema)
  + [Generating the ChatGPT Prompt](#generating-the-chatgpt-prompt)
* [License](#license)

## Prerequisites

* Python 3.11 or higher
* MySQL client (for MySQL databases)
* Pipenv: A Python dependency management tool

## Installation

First, clone the repository:

```bash
git clone https://github.com/chand1012/sql2gpt.git
cd sql2gpt
```

Ensure that you have pipenv installed. If you don't have it installed, you can install it using pip:

```bash
pip install pipenv
```

Once you have pipenv installed, set up the environment and install the dependencies:

```bash
pipenv install
```

To activate the virtual environment, run:

```bash
pipenv shell
```

## Usage

### Adding a Database Connection

Add a new database connection by running:

```bash
python sql2gpt.py add <name> <database_uri>
```

Where `<name>` is the name you want to give to the connection, and `<database_uri>` is the URI for the database, such as:

* PostgreSQL: `postgresql://username:password@localhost/dbname`
* MySQL: `mysql://username:password@localhost/dbname`
* SQLite: `sqlite:///example.db`

### Printing the Schema

To print the schema of a database, run:

```bash
python sql2gpt.py print_schema <database_url or name>
```

Replace <database_url> with the appropriate database URL for your SQL database or the name of the connection you added previously.

### Generating the ChatGPT Prompt

To generate the ChatGPT prompt for a given database, run:

```bash
python sql2gpt.py get_prompt <database_url or name>
```

Replace <database_url> with the appropriate database URL for your SQL database or the name of the connection you added previously. The generated prompt can be passed to ChatGPT to obtain code or ask questions about the database.

## License

This project is licensed under the MIT License.
