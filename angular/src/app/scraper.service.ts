import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { Article } from './models/article';

@Injectable({ providedIn: 'root' })
export class ScraperService {

  private scraperBaseUrl = 'http://localhost:8080/';  // URL to web api

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient) { }

  getArticles(): Observable<Article[]> {
    return this.http.get<Article[]>(this.scraperBaseUrl+'articles');
  }

  scrape(): Observable<Article[]> {
    return this.http.get<Article[]>(this.scraperBaseUrl+'articles/scrape');
  }

  addArticle(article: Article): Observable<Article> {
    return this.http.post<Article>(this.scraperBaseUrl+'articles', article, this.httpOptions);
  }

  deleteArticle(id: number) {
    return this.http.delete(this.scraperBaseUrl+`articles/${id}`, this.httpOptions);
  }

}

