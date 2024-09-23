import { Component, OnInit } from '@angular/core';
import { Article } from '../models/article';
import { ScraperService } from '../scraper.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: [ './dashboard.component.css' ]
})
export class DashboardComponent implements OnInit {
  articles: Article[] = [];

  constructor(private scraperService: ScraperService) { }

  ngOnInit(): void {
    this.getArticles();
  }

  getArticles(): void {
    this.scraperService.getArticles()
      .subscribe(articles => this.articles);
  }
}


