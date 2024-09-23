from fastapi import FastAPI, UploadFile, File, Request
from PIL import Image
from pydantic import BaseModel
from typing import List
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from database import Database
from utils import scrape_articles_util
from datetime import datetime, time, timedelta
import logging
from typing import Optional


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


print('setup ok')
db = Database()

app = FastAPI()

origins = [
    "https://localhost:4000",
    "http://localhost:4000",
    "https://localhost:4200",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Article(BaseModel):
    id: Optional[int] = None
    title: str
    date: datetime

@app.post('/articles')
async def add_article(article: Article):
    """Add Data to Postgres Database
    Args:
        article: Article object to create
    """
    created_article = db.create_article(article)
    
    return created_article

@app.get('/articles')
async def get_articles() -> list[Article]:
    """Get data from database

    Returns:
        data: data stored in Postgres database
    """
    data = db.retrieve()
    
    return data

@app.delete("/articles/{id}")
def delete_article(id: int):
    """Delete data from database

    Returns:
        id: Article id to delete
    """
    db.delete(id)
    
    return id

@app.get("/articles/scrape")
async def scrape_articles() -> list[Article]:
    """Scrape data, save in from database and return all data

    Returns:
        data: data stored in Postgres database
    """
    new_articles = scrape_articles_util()

    for article in new_articles:
        db.create_article(article)
    
    data = db.retrieve()
    
    return data
