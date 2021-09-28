import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Project } from '../data/project';
import { KnowledgeBaseService } from '../knowledge-base.service';

@Component({
  selector: 'app-project-edit',
  templateUrl: './project-edit.component.html',
  styleUrls: ['./project-edit.component.css']
})
export class ProjectEditComponent implements OnInit {
  project?: Project;

  constructor(private activatedRoute: ActivatedRoute, private service: KnowledgeBaseService) { }

  ngOnInit(): void {
    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      throw new Error('id not present in route');
    }
    this.service.getProject(id).subscribe(p => this.project = p);
  }

  onDeleteClick() {
    if (!this.project) {
      throw new Error('project not present');
    }
    this.service.deleteContact(this.project.id).subscribe(_ => window.alert(`Delete Project ${this.project?.name}!`));
  }
}
