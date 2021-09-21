import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-search-results',
  templateUrl: './search-results.component.html',
  styleUrls: ['./search-results.component.css']
})
export class SearchResultsComponent implements OnInit {
  query = '';

  constructor(private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.query = this.activatedRoute.snapshot.paramMap.get('query') || '';
  }
}
