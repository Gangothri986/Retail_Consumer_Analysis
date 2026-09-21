print("SCRIPT STARTED")

import pandas as pd

print("PANDAS IMPORTED")


# ============================================================
# DATA PREPROCESSING FUNCTION
# ============================================================

def preprocess_data(file_path):
    """
    Load the retail customer dataset, clean the data,
    and create additional features required for analysis.
    """

    # --------------------------------------------------------
    # 1. LOAD DATASET
    # --------------------------------------------------------

    df = pd.read_csv(file_path)
  

    print("=" * 60)
    print("DATASET LOADED")
    print("=" * 60)
    

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("=" * 60)
    print("Head:\n",  df.head())
    print("=" * 60)
    print("Info:\n",  df.info())
    print("=" * 60)
    print("Describe\n",  df.describe())
    print("=" * 60)
    print("Describe all\n", df.describe(include='all'))
    print("=" * 60)


    # --------------------------------------------------------
    # 2. HANDLE MISSING VALUES
    # --------------------------------------------------------

    # Fill missing review ratings using the median
    # review rating within each category.

    print("Is null:\n ", df.isnull().sum())
    print("=" * 60)
    df["Review Rating"] = df.groupby("Category")[
        "Review Rating"
    ].transform(
        lambda x: x.fillna(x.median())
    )
    print("Is null:\n ", df.isnull().sum())

    # --------------------------------------------------------
    # 3. STANDARDIZE COLUMN NAMES
    # --------------------------------------------------------

    # Convert column names to lowercase
    # and replace spaces with underscores.
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(" ", "_")

    print("colums:", df.columns)

    # Rename purchase amount column.
    df = df.rename(
        columns={
            "purchase_amount_(usd)": "purchase_amount"
        }
    )
    print("colums:", df.columns)

    # --------------------------------------------------------
    # 4. CREATE AGE GROUP
    # --------------------------------------------------------

    labels = [
        "Young Adult",
        "Adult",
        "Middle-aged",
        "Senior"
    ]

    df["age_group"] = pd.qcut(
        df["age"],
        q=4,
        labels=labels
    )
    print(df[['age', 'age_group']].head(10))

    # --------------------------------------------------------
    # 5. CONVERT PURCHASE FREQUENCY INTO DAYS
    # --------------------------------------------------------

    frequency_mapping = {
        "Fortnightly": 14,
        "Weekly": 7,
        "Monthly": 30,
        "Quarterly": 90,
        "Bi-Weekly": 14,
        "Annually": 365,
        "Every 3 Months": 90
    }

    df["purchase_frequency_days"] = (
        df["frequency_of_purchases"].map(
            frequency_mapping
        )
    )

    print(df[['purchase_frequency_days', 'frequency_of_purchases']].head(10))
    # --------------------------------------------------------
    # 6. DATA CONSISTENCY CHECK
    # -------------------------------------------------------- 

    discount_promo_match = (
        df["discount_applied"]
        == df["promo_code_used"]
    ).all()

    print("\n" + "=" * 60)
    print("DATA CONSISTENCY CHECK")
    print("=" * 60)

    print(
        f"Discount and promo code values match: "
        f"{discount_promo_match}"
    )

    df=df.drop('promo_code_used', axis=1)
    print(df.columns)

    # -----------------------------------------
    # ---------------
    # 7. FINAL DATASET INFORMATION
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("PREPROCESSING COMPLETED")
    print("=" * 60)

    print(f"Final rows: {df.shape[0]}")
    print(f"Final columns: {df.shape[1]}")

    print("\nRemaining missing values:")
    print(df.isnull().sum())

    print("\nFinal columns:")
    print(df.columns.tolist())


    return df


# ============================================================
# RUN DIRECTLY
# ============================================================

print("NAME IS:", __name__)

if __name__ == "__main__":

    print("MAIN BLOCK STARTED")

    file_path = "../data/customer_shopping_behavior.csv"

    df = preprocess_data(file_path)

    print("\nFirst 5 rows of processed data:")
    print(df.head())