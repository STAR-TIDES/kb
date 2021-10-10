import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable } from 'rxjs';
import { Contact } from '../data/contact';
import { Project } from '../data/project';
import { HttpKnowledgeBaseService } from '../http-knowledge-base.service';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-search-results',
  templateUrl: './search-results.component.html',
  styleUrls: ['./search-results.component.css']
})
export class SearchResultsComponent implements OnInit {
  query = '';
  contacts: Contact[] = [];
  projects: Project[] = [];

  constructor(
    private activatedRoute: ActivatedRoute,
    private service: KnowledgeBaseService) { }

  ngOnInit(): void {
    this.query = this.activatedRoute.snapshot.paramMap.get('query') || '';
    this.service.listContacts(this.query).subscribe(cs => this.contacts = cs);
    this.service.listProjects(this.query).subscribe(ps => this.projects = ps);
  }
}
