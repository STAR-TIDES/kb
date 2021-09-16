import { Component, OnInit } from '@angular/core';
import { Contact } from '../data/contact';
import { KnowledgeBaseInterface } from '../knowledge-base-service-interface';
import { KnowledgeBaseService } from '../knowledge-base.service';

@Component({
  selector: 'app-contact-list',
  templateUrl: './contact-list.component.html',
  styleUrls: ['./contact-list.component.css']
})
export class ContactListComponent implements OnInit {
  contacts: Contact[] = [];

  constructor(private client: KnowledgeBaseService) { }

  ngOnInit(): void {
    this.client.listContacts().subscribe(cs => this.contacts = cs);
  }
}
