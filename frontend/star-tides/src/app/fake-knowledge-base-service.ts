import { Injectable } from "@angular/core";
import { Observable, of, throwError } from "rxjs";
import { Availability } from "./data/availability";
import { Contact } from "./data/contact";
import { Guide } from "./data/guide";
import { Project, ProjectStatus } from "./data/project";
import { KnowledgeBaseService } from "./knowledge-base-service";

@Injectable({
    providedIn: 'root',
})
export class FakeKnowledgeBaseService extends KnowledgeBaseService {
    contacts: Contact[] = [];
    projects: Project[] = [];

    static createWithFakeData() {
        const fake = new FakeKnowledgeBaseService();
        fake.contacts = FAKE_CONTACTS;
        fake.projects = FAKE_PROJECTS;
        return fake;
    }

    private newUUID() {
        return Math.random().toString();
    }

    createContact(contact: Contact): Observable<Contact> {
        contact.id = this.newUUID();
        this.contacts.push(contact);
        return of(contact);
    }
    updateProject(id: string, payload: Project): Observable<Project> {
        const i = this.projects.findIndex(p => p.id == id);
        if (i < 0) {
            return throwError(new Error(`project with id ${id} not found`));
        }

        const oldProject = this.projects[i];
        const updated = Object.assign(oldProject, payload);
        this.projects[i] = updated;
        return of(updated);
    }
    deleteProject(id: string): Observable<{}> {
        const before = this.projects.length;
        this.projects = this.projects.filter(p => p.id != id);
        const after = this.projects.length;
        return before != after ? of({}) : throwError(new Error(`project with id ${id} not found`));
    }
    createProject(project: Project): Observable<Project> {
        project.id = this.newUUID();
        this.projects.push(project);
        console.log(this.projects);
        return of(project);
    }

    getGuide(id: string): Observable<Guide> {
        throw new Error("Method not implemented.");
    }
    listGuides(query?: string, pageToken?: string, pageSize?: number): Observable<Guide[]> {
        throw new Error("Method not implemented.");
    }
    updateGuide(id: string, guide: Guide): Observable<Guide> {
        throw new Error("Method not implemented.");
    }
    deleteGuide(id: string): Observable<{}> {
        throw new Error("Method not implemented.");
    }
    createGuide(guide: Guide): Observable<Guide> {
        throw new Error("Method not implemented.");
    }

    getContact(id: string): Observable<Contact> {
        const contact = this.contacts.find(c => c.id == id);
        return contact ? of(contact) : throwError(`contact ${id} not found`);
    }
    listContacts(query?: string, pageToken?: string, pageSize?: number): Observable<Contact[]> {
        if (query) {
            const payload = JSON.parse(query);
            if (payload['id']) {
                const ids = new Set<string>(payload['id']);
                return of(this.contacts.filter(c => ids.has(c.id)));
            }
        }


        return of(this.contacts);
    }
    updateContact(id: string, payload: Contact): Observable<Contact> {
        const i = this.contacts.findIndex(c => c.id == id);
        if (i < 0) {
            return throwError(new Error(`contact with id ${id} not found`));
        }

        const oldContact = this.contacts[i];
        const updated = Object.assign(oldContact, payload);
        this.contacts[i] = updated;
        return of(updated);
    }
    deleteContact(id: string): Observable<{}> {
        let found = false;
        this.contacts = this.contacts.filter(c => {
            if (c.id == id) {
                found = true;
            }
            return c.id != id;
        });
        return found ? of({}) : throwError(`contact with id ${id} not found`);
    }

    getProject(id: string) {
        console.log(this.projects);
        const project = this.projects.find(p => p.id == id);
        return project ? of(project) : throwError(`project ${id} not found`)
    }

    listProjects(query?: string, pageToken?: string, pageSize?: number) {
        return of(this.projects);
    }
}

export const FAKE_CONTACTS: Contact[] = [
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


export const FAKE_PROJECTS: Project[] = [{
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
    notes: 'We are getting WiFi to people who need it!',
    updates: [
        { content: 'Started!', timestamp: new Date('2021-01-02'), editorContactId: '1', requestorContactId: '2' },
        { content: 'Midpoint', timestamp: new Date('2021-05-06'), editorContactId: '1' },
        { content: 'Completed!', timestamp: new Date('2021-09-01'), editorContactId: '1', requestorContactId: '1' },
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