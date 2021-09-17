import { Injectable } from '@angular/core';
import { MatSingleDateSelectionModel } from '@angular/material/datepicker';
import { Observable, of, throwError } from 'rxjs';
import { Contact } from './data/contact';
import { single } from 'rxjs/operators';
import { KnowledgeBaseInterface } from './knowledge-base-service-interface';
import { Availability } from './data/availability';
import { ContactListComponent } from './contact-list/contact-list.component';

@Injectable({
  providedIn: 'root'
})
export class KnowledgeBaseService implements KnowledgeBaseInterface {
  fakeContacts: Contact[] = [
    {
      id: '1',
      name: 'Leo Rudberg',
      location: {
        iso31661CountryCode: 840,
        arbitraryText: "Brooklyn, NY"
      },
      availability: Availability.Available,
      languages: ['English'],
      statuses: ['KB Engineer', 'STAR-TIDES Blah', 'Foo Bar'],
      jobTitle: 'Software Engineer',
      userId: "abc",
      websiteURL: "https://github.com/lozord/me",
      email: "leo@example.com",
      phoneNumber: "1-800-123-4567",
      engagement: {
        locations: [
          { iso31661CountryCode: 840, arbitraryText: "Brooklyn, NY" },
          { iso31661CountryCode: 840, arbitraryText: "Harlem, New York City" },
        ],
        backgrounds: ['Software Engineering', 'Technology'],
        focuses: ['Digital Capacity'],
        areasOfInterest: ['Digital Capacity', 'Technology', 'Nuclear Energy'],
      }
    }, {
      id: '2',
      name: 'Squidward Tentacles',
      location: {
        iso31661CountryCode: 840,
        arbitraryText: 'Bikini Bottom',
      },
      availability: Availability.Unavailable,
      languages: ['English', 'Fish'],
      statuses: [],
      jobTitle: 'Cashier',
      websiteURL: 'https://example.com',
      engagement: {
        locations: [],
        backgrounds: ['Cashier', 'Clarinet'],
        focuses: [],
        areasOfInterest: [],
      }
    }
  ];

  constructor() { }

  getContact(id: string): Observable<Contact> {
    const contact = this.fakeContacts.find(c => c.id == id);
    if (contact) {
      return of(contact);
    }
    return throwError(new Error(`contact with id ${id} not found`));
  }

  listContacts(query = '', pageToken = '', pageSize = 10): Observable<Contact[]> {
    return of(this.fakeContacts);
  }

  updateContact(id: string, contact: Contact): Observable<Contact> {
    throw new Error('unimplemented');
  }

  deleteContact(id: string): Observable<{}> {
    throw new Error('unimplemented');
  }
}
