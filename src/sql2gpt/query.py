"""Read-only query execution with SQL validation."""

import sqlparse
from sqlalchemy import create_engine, text

from sql2gpt import config
from sql2gpt.util import get_db_type


def is_read_only_query(sql: str) -> bool:
    """Validate that a SQL string contains only SELECT statements.

    Returns False for INSERT, UPDATE, DELETE, DDL, and multi-statement queries.
    """
    parsed = sqlparse.parse(sql)

    if not parsed:
        return False

    # Reject multi-statement queries
    if len(parsed) > 1:
        return False

    statement = parsed[0]

    # Get the statement type
    stmt_type = statement.get_type()

    # Only allow SELECT statements
    return stmt_type == "SELECT"


def execute_readonly_query(db_name: str, query: str) -> list[dict]:
    """Execute a read-only query against a configured database.

    Args:
        db_name: Name of database from config
        query: SQL query to execute (must be SELECT only)

    Returns:
        List of row dictionaries

    Raises:
        ValueError: If query is not read-only or database not found
    """
    if not is_read_only_query(query):
        raise ValueError("Only SELECT queries are allowed")

    cfg = config.load()
    database_url = cfg.get(db_name)

    if not database_url:
        raise ValueError(f"Database '{db_name}' not found in config")

    db_type = get_db_type(database_url)

    # Create engine with read-only options where supported
    engine_kwargs = {}
    if db_type in ("postgresql", "postgres"):
        # PostgreSQL supports read-only execution option
        engine_kwargs["execution_options"] = {"postgresql_readonly": True}

    engine = create_engine(database_url, **engine_kwargs)

    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = [dict(row._mapping) for row in result]

    return rows
