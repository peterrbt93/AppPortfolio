# AppPortfolio

The idea of this app is to work as a portfolio viewer, with a simple Angular front-end interface. 
Click through the tabs in the top of the page to view different apps.
</p>
<p>
    All applications run via Docker Compose.

## USAGE

To setup the application, follow the below steps.

First clone the repo :

`git clone https://github.com/peterrbt93/AppPortfolio.git`

Now run the app with Docker Compose, by running the following commands in a terminal in the main directory:

`docker compose up -d --build db` - wait for it to build

`docker compose up -d --build`

You should now have 

Angular frontend running at `http://localhost:4000/`
Python FastAPI backend running at `http://localhost:8080/`
Postgres DB running at `http://localhost:5432/`

A Swagger page for the backend can be found at `http://localhost:8080/docs`

## Scraper app

This page works as an interface to a backend application that "scrapes" and stores article titles in a postgres DB.
    The user can add articles manually by typing in a title and clicking "Add article" button. The
    "Scrape articles" button scrapes the first 5 articles from <a href="https://nyheder.tv2.dk/seneste" target="_blank"> Tv2 Nyhedernes Seneste page</a> and adds them to the list.

