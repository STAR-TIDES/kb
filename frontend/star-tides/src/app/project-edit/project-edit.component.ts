import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Project, ProjectStatus, STATUS_LIST } from '../data/project';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-project-edit',
  templateUrl: './project-edit.component.html',
  styleUrls: ['./project-edit.component.css']
})
export class ProjectEditComponent implements OnInit {
  project?: Project;
  isNew = false;
  readonly STATUS_LIST = STATUS_LIST;

  constructor(
    private activatedRoute: ActivatedRoute,
    private router: Router,
    private service: KnowledgeBaseService) { }

  ngOnInit(): void {
    const isNew = this.activatedRoute.snapshot.routeConfig?.path?.includes('/new');
    if (isNew) {
      this.isNew = true;
      this.project = {
        id: '',
        name: '',
        location: {
          iso31661CountryCode: 0,
          arbitraryText: '',

        },
        contacts: [],
        engagement: {
          areasOfInterest: [],
          focuses: [],
          locations: [],
          backgrounds: [],
        },
        summary: '',
        status: ProjectStatus.Proposed,
      };
      return;
    }

    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      console.error('id not present in route');
      this.router.navigate(['/projects']);
      return;
    }
    this.service.getProject(id).subscribe(p => this.project = p);
  }

  onUpdateClick() {
    if (!this.project) {
      throw new Error('project not present');
    }
    this.service.updateProject(this.project.id, this.project)
      .subscribe(p => this.router.navigate(['/projects', p.id]));
  }

  onDeleteClick() {
    if (!this.project) {
      throw new Error('project not present');
    }
    this.service.deleteProject(this.project.id)
      .subscribe(_ => this.router.navigate(['/projects']));
  }

  onCreateClick() {
    this.service.createProject(this.project!!)
      .subscribe(
        p => this.router.navigate(['/projects', p.id]),
        err => console.error(err));
  }
}
