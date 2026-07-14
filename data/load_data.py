import snowflake.connector
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas
from getpass import getpass



# Connect to Snowflake
conn = snowflake.connector.connect(
    account="DJQWKNN-AA74051",
    user="MAINABOROKHA",
    password = getpass("Enter your Snowflake password: "),
    role="ACCOUNTADMIN",
    warehouse="COMPUTE_WH",
    database="FINSIGHT_DB",
    schema="PUBLIC",
    authenticator="username_password_mfa"
)

print("Connected to Snowflake!")

# Load Superstore
print("⏳ Loading Superstore data...")
df_store = pd.read_csv("data/superstore.csv", encoding="latin1")
df_store.columns = [c.upper().replace(" ", "_").replace("-", "_") for c in df_store.columns]
df_store["ORDER_DATE"] = pd.to_datetime(df_store["ORDER_DATE"]).dt.date
df_store["SHIP_DATE"] = pd.to_datetime(df_store["SHIP_DATE"]).dt.date
success, nchunks, nrows, _ = write_pandas(conn, df_store, "SUPERSTORE_SALES")
print(f"Superstore loaded: {nrows} rows")

# Load Financial Sample
print("⏳ Loading Financial Sample data...")
df_fin = pd.read_csv("data/financial_sample.csv")
df_fin.columns = [c.upper().strip().replace(" ", "_").replace("-", "_") for c in df_fin.columns]
df_fin["DATE"] = pd.to_datetime(df_fin["DATE"]).dt.date
success, nchunks, nrows, _ = write_pandas(conn, df_fin, "FINANCIAL_SAMPLE")
print(f"Financial Sample loaded: {nrows} rows")

print("\nAll data loaded successfully!")
conn.close()
