from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import run_query
from cortex import generate_sql, generate_insight

app = FastAPI(title="FinSight AI", version="1.0.0")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class QuestionRequest(BaseModel):
    question: str

# Health check
@app.get("/")
def root():
    return {"status": "FinSight AI is running 🚀"}

# Main AI endpoint
@app.post("/ask")
def ask(request: QuestionRequest):
    try:
        # Step 1: Convert question to SQL using Cortex
        sql = generate_sql(request.question)

        # Step 2: Run the SQL against Snowflake
        data = run_query(sql)

        # Step 3: Generate insight from results
        insight = generate_insight(request.question, data)

        return {
            "question": request.question,
            "sql": sql,
            "data": data,
            "insight": insight
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get available tables
@app.get("/tables")
def get_tables():
    data = run_query("""
        SELECT TABLE_NAME, ROW_COUNT 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_SCHEMA = 'PUBLIC'
    """)
    return data