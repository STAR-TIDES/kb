import { Component, OnInit } from '@angular/core';
import { Contact } from '../data/contact';
import { KnowledgeBaseService } from '../knowledge-base-service';
import { HttpKnowledgeBaseService } from '../http-knowledge-base.service';

@Component({
  selector: 'app-contact-list',
  templateUrl: './contact-list.component.html',
  styleUrls: ['./contact-list.component.css']
})
export class ContactListComponent implements OnInit {
  contacts: Contact[] = [];

  constructor(private client: KnowledgeBaseService) { }

  ngOnInit(): void {
    this.client.listContacts().subscribe(cs => this.contacts = cs, err => console.error(err));
  }
}
