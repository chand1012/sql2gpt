"""FastMCP server exposing database schema and read-only query execution."""

import argparse

from fastmcp import FastMCP

from sql2gpt import config
from sql2gpt.util import get_db_type
from sql2gpt import get_schemas


mcp = FastMCP("sql2gpt")


@mcp.resource("sql2gpt://databases")
def list_databases() -> str:
    """List all configured databases with their types (not full URIs)."""
    cfg = config.load()
    if not cfg:
        return "No databases configured. Use add_database tool to add one."

    lines = []
    for name, uri in cfg.items():
        db_type = get_db_type(uri)
        lines.append(f"{name}: {db_type}")

    return "\n".join(lines)


@mcp.resource("sql2gpt://{db_name}/schema")
def get_database_schema(db_name: str) -> str:
    """Get the full schema for a configured database."""
    cfg = config.load()
    database_url = cfg.get(db_name)

    if not database_url:
        return f"Database '{db_name}' not found in config"

    schemas = get_schemas(database_url, quiet=True)
    return "\n".join(schemas)


@mcp.resource("sql2gpt://{db_name}/tables")
def list_tables(db_name: str) -> str:
    """List table names for a configured database."""
    cfg = config.load()
    database_url = cfg.get(db_name)

    if not database_url:
        return f"Database '{db_name}' not found in config"

    schemas = get_schemas(database_url, quiet=True)
    # Extract just table names from schema strings like "table_name(col1 type1, ...)"
    table_names = [s.split("(")[0] for s in schemas]
    return "\n".join(table_names)


@mcp.tool()
def execute_query(db_name: str, query: str) -> dict:
    """Execute a read-only SELECT query against a configured database.

    Args:
        db_name: Name of the database (as configured via add_database)
        query: SQL SELECT query to execute

    Returns:
        Dict with success, data (list of row dicts), and row_count
    """
    # Import here to avoid circular imports
    from sql2gpt.query import execute_readonly_query

    try:
        rows = execute_readonly_query(db_name, query)
        return {
            "success": True,
            "data": rows,
            "row_count": len(rows),
        }
    except ValueError as e:
        return {
            "success": False,
            "error": str(e),
            "data": [],
            "row_count": 0,
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Query execution failed: {e}",
            "data": [],
            "row_count": 0,
        }


@mcp.tool()
def add_database(name: str, uri: str) -> dict:
    """Add a new database connection to the configuration.

    Args:
        name: Friendly name for the database
        uri: Database connection URI (e.g., postgresql://user:pass@host/db)

    Returns:
        Dict with success status and message
    """
    try:
        config.add(name, uri)
        return {
            "success": True,
            "message": f"Database '{name}' added successfully",
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
        }


def main():
    parser = argparse.ArgumentParser(description="sql2gpt MCP server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="Transport mode (default: stdio)",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host for HTTP transport (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for HTTP transport (default: 8000)",
    )
    args = parser.parse_args()

    if args.transport == "http":
        mcp.run(transport="http", host=args.host, port=args.port)
    else:
        mcp.run()


if __name__ == "__main__":
    main()
