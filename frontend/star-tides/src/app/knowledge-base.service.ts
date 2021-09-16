import { Injectable } from '@angular/core';
import { MatSingleDateSelectionModel } from '@angular/material/datepicker';
import { Observable, of, throwError } from 'rxjs';
import { Contact } from './data/contact';
import { single } from 'rxjs/operators';
import { KnowledgeBaseInterface } from './knowledge-base-service-interface';

@Injectable({
  providedIn: 'root'
})
export class KnowledgeBaseService implements KnowledgeBaseInterface {
  fakeContacts: Contact[] = [];

  constructor() { }

  getContact(id: string): Observable<Contact> {
    const contact = this.fakeContacts.find(c => c.id == id);
    if (contact) {
      return of(contact);
    }
    return throwError(new Error(`contact with id ${id} not found`));
  }

  listContacts(query = '', pageToken = '', pageSize = 10): Observable<Contact[]> {
    throw new Error('unimplementeed');
  }

  updateContact(id: string, contact: Contact): Observable<Contact> {
    throw new Error('unimplemented');
  }

  deleteContact(id: string): Observable<{}> {
    throw new Error('unimplemented');
  }
}
