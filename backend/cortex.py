import os
from dotenv import load_dotenv
from database import get_connection

load_dotenv()

# This tells Cortex about your tables so it can write correct SQL
SCHEMA_CONTEXT = """
You are a financial data analyst AI. You have access to these Snowflake tables:

1. SUPERSTORE_SALES (9994 rows):
   - ROW_ID, ORDER_ID, ORDER_DATE, SHIP_DATE, SHIP_MODE
   - CUSTOMER_ID, CUSTOMER_NAME, SEGMENT, COUNTRY, CITY, STATE
   - POSTAL_CODE, REGION, PRODUCT_ID, CATEGORY, SUB_CATEGORY
   - PRODUCT_NAME, SALES, QUANTITY, DISCOUNT, PROFIT

2. FINANCIAL_SAMPLE (700 rows):
   - SEGMENT, COUNTRY, PRODUCT, DISCOUNT_BAND
   - UNITS_SOLD, MANUFACTURING_PRICE, SALE_PRICE
   - GROSS_SALES, DISCOUNTS, SALES, COGS, PROFIT
   - DATE, MONTH_NUMBER, MONTH_NAME, YEAR

Always write Snowflake-compatible SQL.
Always return only the SQL query, nothing else.
"""

def generate_sql(question: str) -> str:
    """Use Cortex to convert natural language to SQL"""
    conn = get_connection()
    cursor = conn.cursor()

    prompt = f"{SCHEMA_CONTEXT}\n\nUser question: {question}\n\nSQL:"

    cursor.execute("""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3.1-70b',
            %s
        )
    """, (prompt,))

    result = cursor.fetchone()[0]
    conn.close()

    # Clean up the SQL response
    sql = result.strip()
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql


def generate_insight(question: str, data: dict) -> str:
    """Use Cortex to generate a human-readable insight from query results"""
    conn = get_connection()
    cursor = conn.cursor()

    data_summary = f"Columns: {data['columns']}\nFirst 5 rows: {data['rows'][:5]}"

    prompt = f"""
You are a financial analyst. A user asked: "{question}"
Here is the data returned from the database:
{data_summary}

Write a clear, concise 2-3 sentence insight summarizing what this data means 
for the business. Be specific with numbers.
"""

    cursor.execute("""
        SELECT SNOWFLAKE.CORTEX.COMPLETE(
            'llama3.1-70b',
            %s
        )
    """, (prompt,))

    insight = cursor.fetchone()[0]
    conn.close()
    return insight.strip()