from sqlalchemy import create_engine

from data_preprocessing import preprocess_data


# ============================================================
# FILE PATH
# ============================================================

file_path = "../data/customer_shopping_behavior.csv"


# ============================================================
# PREPROCESS DATA
# ============================================================

df = preprocess_data(file_path)


# ============================================================
# SQL SERVER CONNECTION
# ============================================================

server = r"localhost\SQLEXPRESS"
database = "customer_behaviour"

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)


# ============================================================
# LOAD DATA INTO SQL SERVER
# ============================================================

df.to_sql(
    name="customer_data",
    con=engine,
    if_exists="replace",
    index=False
)


# ============================================================
# SUCCESS MESSAGE
# ============================================================

print("\n" + "=" * 60)
print("SUCCESS")
print("=" * 60)

print("Cleaned data loaded into SQL Server successfully!")
print(f"Rows loaded: {len(df)}")
print(f"Columns loaded: {len(df.columns)}")

engine.dispose()