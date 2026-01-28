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

* Python 3.10 or higher

## Installation

### Via uvx (no install needed)

```bash
uvx sql2gpt get_prompt postgresql://user:pass@localhost/mydb
```

### Via pip/uv

```bash
pip install sql2gpt
# or
uv pip install sql2gpt
```

### From source

```bash
git clone https://github.com/chand1012/sql2gpt.git
cd sql2gpt
uv sync
uv run sql2gpt --help
```

## Database URLs

- PostgreSQL: `postgresql://user:pass@localhost/dbname`
- MySQL: `mysql+pymysql://user:pass@localhost/dbname`
- SQLite: `sqlite:///path/to/db.sqlite`

**Note:** MySQL URLs must use `mysql+pymysql://` prefix (not just `mysql://`).

## Usage

### Adding a Database Connection

Add a new database connection by running:

```bash
sql2gpt add <name> <database_uri>
```

Where `<name>` is the name you want to give to the connection, and `<database_uri>` is the URI for the database.

### Printing the Schema

To print the schema of a database, run:

```bash
sql2gpt print_schema <database_url or name>
```

Replace `<database_url>` with the appropriate database URL for your SQL database or the name of the connection you added previously.

### Generating the ChatGPT Prompt

To generate the ChatGPT prompt for a given database, run:

```bash
sql2gpt get_prompt <database_url or name>
```

Replace `<database_url>` with the appropriate database URL for your SQL database or the name of the connection you added previously. The generated prompt can be passed to ChatGPT to obtain code or ask questions about the database.

## License

This project is licensed under the MIT License.
