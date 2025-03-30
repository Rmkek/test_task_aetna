from fastapi import FastAPI, Query
from sqlalchemy import select
from main import engine, insurance_data
from typing import List, Dict, Any

app = FastAPI()

@app.get("/fetch_data")
async def fetch_data(
    offset: int = Query(default=0, ge=0, description="Number of records to skip"),
    batch_size: int = Query(default=100, ge=1, le=1000, description="Number of records to return")
) -> List[Dict[Any, Any]]:
    print('before query')
    query = select(insurance_data).offset(offset).limit(batch_size)
    
    print('query', query)
    print('engine', engine)

    with engine.connect() as connection:
        result = connection.execute(query)
        records = [dict(row) for row in result]
    
    return records 