import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { of, throwError } from 'rxjs';
import { mergeMap } from 'rxjs/operators';
import { Contact } from '../data/contact';
import { Project } from '../data/project';
import { KnowledgeBaseService } from '../knowledge-base.service';

@Component({
  selector: 'app-project-detail',
  templateUrl: './project-detail.component.html',
  styleUrls: ['./project-detail.component.css']
})
export class ProjectDetailComponent implements OnInit {
  project?: Project;

  constructor(private activatedRoute: ActivatedRoute, private router: Router, private client: KnowledgeBaseService) { }

  ngOnInit(): void {
    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      console.error('id not present in route');
      this.router.navigate(['/projects']);
    }

    this.client.getProject(id!).subscribe(
      project => this.project = project,
      err => console.error(err)
    );
  }
}
