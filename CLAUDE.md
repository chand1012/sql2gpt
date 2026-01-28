# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SQL2GPT extracts SQL database schemas and formats them as prompts for ChatGPT. It supports PostgreSQL, MySQL, and SQLite databases.

## Commands

### Development
```bash
uv sync              # Install dependencies
uv run sql2gpt       # Run CLI
```

### Build and Publish
```bash
uv run python -m build   # Build distribution
rm -rf dist sql2gpt.egg-info  # Clean
uv run twine upload dist/*    # Upload to PyPI
```

### CLI Usage
```bash
# Via installed package
sql2gpt add mydb postgresql://user:pass@localhost/dbname
sql2gpt get_prompt mydb
```

## Architecture

```
src/sql2gpt/
  __init__.py  → Main CLI (fire.Fire auto-generates commands from SQL2GPT class methods)
  config.py    → Persists database connections to ~/.sql2gpt/dbs.json
  util.py      → URL parsing helpers (get_db_type, is_uri)
```

**Data flow for `get_prompt`:**
1. Resolve database name → URI via config
2. Connect with SQLAlchemy and inspect tables/columns
3. Format schema as `table_name(col1 type1, col2 type2, ...)`
4. Insert into prompt template with database type

## Key Patterns

- **CLI generation**: Google Fire converts class methods to CLI commands automatically
- **Database abstraction**: SQLAlchemy's `inspect()` handles all database types uniformly
- **Named connections**: Users can save URIs with friendly names via `add` command
