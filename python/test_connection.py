
import pandas as pd
from sqlalchemy import create_engine

# =========================

# SERVER + DATABASE
# =========================

server = r'localhost\SQLEXPRESS'
database = 'customer_behaviour'

# =========================
# CONNECTION STRING
# =========================

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# =========================
# CREATE ENGINE
# =========================

engine = create_engine(connection_string)

# =========================
# TEST CONNECTION
# =========================

query = "SELECT name FROM sys.tables"

df = pd.read_sql(query, engine)

print("CONNECTION SUCCESSFUL!")
print(df)
