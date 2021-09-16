import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { throwError } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { Contact } from '../data/contact';
import { KnowledgeBaseInterface } from '../knowledge-base-service-interface';
import { KnowledgeBaseService } from '../knowledge-base.service';

@Component({
  selector: 'app-contact-detail',
  templateUrl: './contact-detail.component.html',
  styleUrls: ['./contact-detail.component.css']
})
export class ContactDetailComponent implements OnInit {
  contact?: Contact;

  constructor(private route: ActivatedRoute, private client: KnowledgeBaseService) { }

  ngOnInit(): void {
    this.route.params.pipe(switchMap(params => {
      const id: string | undefined = params['id'];
      if (id) {
        return this.client.getContact(id);
      } else {
        return throwError('id not present from route');
      }
    })).subscribe(contact => this.contact = contact, err => console.error(err));
  }
}
