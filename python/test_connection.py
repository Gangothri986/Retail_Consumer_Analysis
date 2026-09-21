from sqlalchemy import create_engine
import pandas as pd


# ============================================================
# SQL SERVER CONFIGURATION
# ============================================================

server = r"localhost\SQLEXPRESS"
database = "customer_behaviour"


# ============================================================
# DATABASE CONNECTION
# ============================================================

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)


# ============================================================
# TEST DATABASE CONNECTION
# ============================================================

try:
    query = "SELECT name FROM sys.tables"

    tables = pd.read_sql(query, engine)

    print("=" * 60)
    print("DATABASE CONNECTION SUCCESSFUL!")
    print("=" * 60)

    print("\nTables in the database:")

    if tables.empty:
        print("No tables found.")
    else:
        print(tables.to_string(index=False))

except Exception as e:
    print("=" * 60)
    print("DATABASE CONNECTION FAILED")
    print("=" * 60)

    print("\nError:")
    print(e)

finally:
    engine.dispose()