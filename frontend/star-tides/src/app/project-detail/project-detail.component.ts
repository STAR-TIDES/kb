import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { of } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { Contact } from '../data/contact';
import { Project } from '../data/project';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-project-detail',
  templateUrl: './project-detail.component.html',
  styleUrls: ['./project-detail.component.css']
})
export class ProjectDetailComponent implements OnInit {
  project?: Project;
  idToContactMap: Map<string, Contact> = new Map();

  constructor(
    private activatedRoute: ActivatedRoute,
    private router: Router,
    private client: KnowledgeBaseService) { }

  ngOnInit(): void {
    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      console.error('id not present in route');
      this.router.navigate(['/projects']);
    }

    const obs = this.client.getProject(id!);
    obs.subscribe(project => this.project = project, err => console.error(err));
    obs.pipe(switchMap(project => {
      if (!project.updates) {
        return of([]);
      }

      const ids = new Set<string>();
      for (const update of project.updates) {
        ids.add(update.editorContactId);
        if (update.requestorContactId) {
          ids.add(update.requestorContactId);
        }
      }

      const query = {
        'id': Array.from(ids)
      };

      return this.client.listContacts(JSON.stringify(query));
    })).subscribe(contacts => {
      for (const contact of contacts) {
        this.idToContactMap.set(contact.id, contact);
      }
    }, err => console.error('contact lookup error!', err));
  }

  getContactName(id: string) {
    const contact = this.idToContactMap.get(id);
    if (!contact) {
      return 'Unknown';
    }
    return contact.name;
  }
}
