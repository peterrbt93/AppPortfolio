import { Component, OnInit } from '@angular/core';

import { Article } from '../models/article';
import { ScraperService } from '../scraper.service';
import { formatDate } from '@angular/common';


@Component({
  selector: 'app-scraper',
  templateUrl: './scraper.component.html',
  styleUrls: ['./scraper.component.css']
})
export class ScraperComponent implements OnInit {
  articles: Article[] = [];

  constructor(private scraperService: ScraperService) { }

  ngOnInit(): void {
    this.getArticles();
  }

  getArticles(): void {
    this.scraperService.getArticles()
    .subscribe(articles => this.articles = articles);
  }

  formatDate(date: Date): any {
    return formatDate(date, 'yyyy-MM-dd', 'en-US')
  }

  scrape(): void {
    this.scraperService.scrape()
    .subscribe(articles => this.articles = articles);
  }

  add(title: string): void {
    title = title.trim();
    if (!title) { return; }
    let date = new Date();
    date.setHours(date.getHours()+2)
    this.scraperService.addArticle({ title , date} as Article)
      .subscribe(article => {
        this.getArticles();
      });
  }

  deleteArticle(id: number): void {
    this.scraperService.deleteArticle(id).subscribe(() => {
      console.log("Article deleted")
      this.articles = this.articles.filter(a => a.id != id)
    });
  }


}


 