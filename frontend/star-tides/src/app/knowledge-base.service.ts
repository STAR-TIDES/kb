import { Injectable } from '@angular/core';
import { MatSingleDateSelectionModel } from '@angular/material/datepicker';
import { Observable, of, throwError } from 'rxjs';
import { Contact } from './data/contact';
import { single } from 'rxjs/operators';
import { KnowledgeBaseInterface } from './knowledge-base-service-interface';
import { Availability } from './data/availability';
import { ContactListComponent } from './contact-list/contact-list.component';
import { Project, ProjectStatus } from './data/project';
import { HttpClient } from '@angular/common/http';

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

  fakeProjects: Project[] = [{
    id: '1',
    name: 'Delivering Digital Capacity',
    contacts: [{ id: '1', name: 'Leo Rudberg' }, { name: 'Darth Vader' }],
    summary: 'Doing awesome work with technology!',
    engagement: {
      locations: [{ iso31661CountryCode: 840, arbitraryText: 'New York City' }],
      focuses: ['Digital Capacity'],
      backgrounds: ['Foo'],
      areasOfInterest: ['Bar'],
    },
    location: { iso31661CountryCode: 840, arbitraryText: 'New York City' },
    status: ProjectStatus.Completed,
    updates: [
      { content: 'Started!', timestamp: new Date('2021-01-02'), userId: '1', requestingContactId: '2' },
      { content: 'Midpoint', timestamp: new Date('2021-05-06'), userId: '1' },
      { content: 'Completed!', timestamp: new Date('2021-09-01'), userId: '1', requestingContactId: '1' },
    ]
  }, {
    id: '2',
    name: 'Water Here!',
    contacts: [{ name: 'Marco Polo' }, { name: 'Squidward Tentacles', id: '2' }],
    summary: 'Bringing water to your crops.',
    engagement: {
      locations: [
        { iso31661CountryCode: 123, arbitraryText: 'Some Place' },
        { iso31661CountryCode: 456, arbitraryText: 'Some Other Place' }
      ],
      focuses: ['Agriculture', 'Water', 'Health and Sanitation'],
      backgrounds: ['Government', 'Research'],
      areasOfInterest: ['Agriculture'],
    },
    location: { iso31661CountryCode: 123, arbitraryText: 'Some Place' },
    status: ProjectStatus.InProgressHelpWanted,
    solutionCosts: 'Water pumps for __$200 each__.'
  }];

  constructor() { }

  getContact(id: string): Observable<Contact> {
    const contact = this.fakeContacts.find(c => c.id == id);
    if (contact) {
      return of(contact);
    }
    return throwError(new Error(`contact with id ${id} not found`));
  }

  listContacts(query = '', pageToken = '', pageSize = 10): Observable<Contact[]> {
    if (query == '') {
      return of(this.fakeContacts);
    }

    return of(this.fakeContacts.filter(c => JSON.stringify(c).includes(query)));
  }

  updateContact(id: string, contact: Contact): Observable<Contact> {
    const index = this.fakeContacts.findIndex(c => c.id == id);
    if (index < 0) {
      return throwError(`failed to find contact with id ${id}`);
    }
    this.fakeContacts[index] = contact;
    return of(contact);
  }

  deleteContact(id: string): Observable<{}> {
    let found = false;
    this.fakeContacts = this.fakeContacts.filter(c => {
      if (c.id == id) {
        found = true;
      }
      return c.id != id;
    });
    return found ? of({}) : throwError(`contact with id ${id} not found`);
  }

  getProject(id: string): Observable<Project> {
    const project = this.fakeProjects.find(p => p.id == id);
    if (project) {
      return of(project);
    }
    return throwError(new Error(`project with id ${id} not found`));
  }

  listProjects(query = '', pageToken = '', pageSize = 10): Observable<Project[]> {
    if (query == '') {
      return of(this.fakeProjects);
    }
    return of(this.fakeProjects.filter(p => JSON.stringify(p).includes(query)));
  }
}
