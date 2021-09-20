import { Component, OnInit } from '@angular/core';
import { Project } from '../data/project';
import { KnowledgeBaseService } from '../knowledge-base.service';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  styleUrls: ['./project-list.component.css']
})
export class ProjectListComponent implements OnInit {
  projects: Project[] = [];

  constructor(private client: KnowledgeBaseService) { }

  ngOnInit(): void {
    this.client.listProject().subscribe(
      projects => this.projects = projects,
      err => console.error(err),
    )
  }
}
