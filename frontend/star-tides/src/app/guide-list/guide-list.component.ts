import { Component, OnInit } from '@angular/core';
import { switchMap } from 'rxjs/operators';
import { Contact } from '../data/contact';
import { Guide } from '../data/guide';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-guide-list',
  templateUrl: './guide-list.component.html',
  styleUrls: ['./guide-list.component.css']
})
export class GuideListComponent implements OnInit {
  guides: Guide[] = [];
  idToContactMap = new Map<string, Contact>();

  constructor(private service: KnowledgeBaseService) { }

  ngOnInit(): void {
    const obs = this.service.listGuides();
    obs.subscribe(gs => this.guides = gs);
    obs.pipe(switchMap(gs => {
      const ids = new Set();
      for (const guide of gs) {
        ids.add(guide.id);
      }

      const query = {
        'id': Array.from(ids)
      };

      return this.service.listContacts(JSON.stringify(query));
    })).subscribe(contacts => {
      for (const contact of contacts) {
        this.idToContactMap.set(contact.id, contact);
      }
    });
  }

  getAuthorName(authorId: string): string {
    const contact = this.idToContactMap.get(authorId);
    if (!contact) {
      return 'Unknown';
    }
    return contact.name;
  }
}
