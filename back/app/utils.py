import re
import numpy as np
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, time, timedelta
import requests
from bs4 import BeautifulSoup


class Article(BaseModel):
    id: Optional[int] = None
    title: str
    date: datetime

def scrape_articles_util() :
    """Scrape data before storing them into Postgres database

    Returns:
        final_data: data to store into Postgres database
    """
    
    print("Scraping  top 5 articles...")

    url = 'https://nyheder.tv2.dk/seneste'
    r = requests.get(url)
    content = r.content

    # Create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(content.decode('utf-8','ignore'), features="html.parser")

    result_list = []
    max_return_num = 5
    title_elements = soup.select('h3 span')[:max_return_num]
    for element in title_elements:
        result_list.append(Article(id=0,title=element.text.replace('\\', ''),date=datetime.now()))

    
    return result_list