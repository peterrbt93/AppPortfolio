from fastapi import HTTPException
from sqlalchemy import create_engine, insert, text, MetaData, select
from sqlalchemy.ext.automap import automap_base
import pandas as pd
from datetime import datetime, time, timedelta
from typing import Optional
from pydantic import BaseModel
import logging



logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

class Article(BaseModel):
    id: Optional[int] = None
    title: str
    date: datetime

class Database() :
    
    def __init__(self):

        self.engine = create_engine('postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format("postgres", "Welcome", "postgres", 5432, "myDB"))
        self.conn = self.engine.connect()
        self.meta_data = MetaData(bind=self.conn)
        self.add_data = []

        
    def create_article(self, article: Article):
        """Add information to Postgres database

                Returns:
            data: data added in Postgres database
        """
        self.conn.execute(
                    "INSERT INTO articles (title, date) VALUES (%s, %s)",
                    (article.title, article.date),
                )
        return article
            
                

    def retrieve(self) :
        """Retrieve informations to Postgres database

                Returns:
            data: data stored in Postgres database
        """
        data = self.conn.execute("SELECT * FROM articles ORDER BY DATE DESC").fetchall()
        return data
    
    def delete(self, id: int):
        """Delete information to Postgres database

                Returns:
            data: data stored in Postgres database
        """
        
        user = self.conn.execute("SELECT * FROM articles where id=%s",id).fetchall()
        if not user:
            raise HTTPException(status_code=404, detail="Article not found")
        self.conn.execute("DELETE FROM articles where id=%s",id)
        return id
    
    