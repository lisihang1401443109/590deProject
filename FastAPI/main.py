# Fast API 
from fastapi import FastAPI
from dotenv import load_dotenv

from utils import get_db, get_s3_client


def authenticate(token: str):
    engine = get_db()
    with engine.connect() as conn:
        result = conn.execute("SELECT * FROM users WHERE token = :token", {"token": token})
        return result.fetchone()    
    
    
app = FastAPI()