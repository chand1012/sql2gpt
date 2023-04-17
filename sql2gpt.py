import fire
from sqlalchemy import create_engine, MetaData, Table, inspect

import config
from util import get_db_type, is_uri


def get_schemas(database_url):
    print("Connecting to database...")
    engine = create_engine(database_url)
    meta = MetaData()

    print("Inspecting database...")
    inspector = inspect(engine)
    schemas = []
    for table_name in inspector.get_table_names():
        table = Table(table_name, meta, autoload_with=engine)
        schema_string = f"{table_name}("
        columns = []
        for column in table.columns:
            columns.append(f"{column.name} {column.type}")
        schema_string += ", ".join(columns) + ")"
        schemas.append(schema_string)

    print("Done")
    print('-'*80)
    return schemas


class SQL2GPT:
    def __init__(self):
        self.config = config.load()
        self.prompt = "I have a {} SQL database. I am going to give you the schema in the following format: table_name(column_name column_type, column_name column_type, ...), followed by END. After END, you will be given instructions on how to use the schema information. Here is the schema:\n\n{}\nEND"

    def get_uri(self, i) -> str | None:
        database_url = i
        if not is_uri(database_url):
            database_url = self.config.get(database_url, None)
            if not database_url:
                print(
                    "Database not found in URL. Add with `sql2gpt add <name> <database_uri>`.")
                return None
        return database_url

    def print_schema(self, database_url):
        database_url = self.get_uri(database_url)
        schemas = get_schemas(database_url)
        print("\n".join(schemas))

    def get_prompt(self, database_url):
        database_url = self.get_uri(database_url)
        db_type = get_db_type(database_url)
        schemas = get_schemas(database_url)
        print(self.prompt.format(db_type, "\n".join(schemas)))

    def add(self, name: str, database_uri: str):
        config.add(name, database_uri)
        print("Database added successfully.")


if __name__ == "__main__":
    fire.Fire(SQL2GPT)
