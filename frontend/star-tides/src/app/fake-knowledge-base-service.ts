import { Injectable } from "@angular/core";
import { Observable, of, throwError } from "rxjs";
import { Availability } from "./data/availability";
import { Contact } from "./data/contact";
import { Guide } from "./data/guide";
import { Project, ProjectStatus } from "./data/project";
import { FakeActivatedRouteProvider } from "./fake-activated-route";
import { KnowledgeBaseService } from "./knowledge-base-service";

@Injectable({
    providedIn: 'root',
})
export class FakeKnowledgeBaseService extends KnowledgeBaseService {
    contacts: Contact[] = [];
    projects: Project[] = [];
    guides: Guide[] = [];

    static createWithFakeData() {
        const fake = new FakeKnowledgeBaseService();
        fake.contacts = FAKE_CONTACTS;
        fake.projects = FAKE_PROJECTS;
        fake.guides = FAKE_GUIDES;
        return fake;
    }

    // From https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random#getting_a_random_integer_between_two_values.
    private getRandomInt(min = 5, max = 5000) {
        const _min = Math.ceil(min);
        const _max = Math.floor(max);
        return Math.floor(Math.random() * (_max - _min + 1) + _min);
    }

    private newUUID() {
        return this.getRandomInt().toString();
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
        const guide = this.guides.find(g => g.id == id);
        return guide ? of(guide) : throwError(`guide ${id} not found`);
    }
    listGuides(query?: string, pageToken?: string, pageSize?: number): Observable<Guide[]> {
        return of(this.guides);
    }
    updateGuide(id: string, guide: Guide): Observable<Guide> {
        const i = this.guides.findIndex(g => g.id == id);
        if (i < 0) {
            return throwError(new Error(`project with id ${id} not found`));
        }

        const oldGuide = this.guides[i];
        const updated = Object.assign(oldGuide, guide);
        this.guides[i] = updated;
        return of(updated);
    }
    deleteGuide(id: string): Observable<{}> {
        const before = this.guides.length;
        this.guides = this.guides.filter(g => g.id != id);
        const after = this.guides.length;
        return before != after ? of({}) : throwError(new Error(`guide with id ${id} not found`));
    }
    createGuide(guide: Guide): Observable<Guide> {
        guide.id = this.newUUID();
        this.guides.push(guide);
        return of(guide);
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

export const FAKE_GUIDES: Guide[] = [
    {
        id: '1',
        name: 'Project Eagle Feather',
        author: '1',
        summary: `In [Project Eagle Feather](https://peoplecentered.net/tag/project-eagle-feather/),
            we are working with a _diverse_ array of indigenous Americans to work towards
            __better__ digital capacity!
            Here's a _cool_ image:\n\n\n![Some network systems!](https://peoplecentered.net/wp-content/uploads/2020/01/TDVN-640x380.png)
            And here's some more content. Hello world\n## One header.\n### Another header.\nSome paragraph content.\n- And\n- A\n- List!`,
        engagement: {
            locations: [{ iso31661CountryCode: 840, arbitraryText: 'California' }],
            areasOfInterest: ['Blah'],
            focuses: ['Digital Capacity'],
            backgrounds: ['Lorem Ipsum'],
        },
        relatedProjects: ['1'],
        relevantContacts: ['2'],
        guidances: [
            { content: 'First is that you _have_ to meet with stakeholders!' },
            {
                content: `Next, you should meet with the tribes' leadership.`,
                options: [
                    { name: 'Meet with tribal elders?', content: '' },
                    { name: 'Meet with local government?', content: '' },
                ]
            },
            { content: `Next, you start to look into technology.` },
            {
                content: `Finally, Do you go with satellite or fixed network?`,
                options: [
                    { name: 'Satellite Internet', content: 'Satellite has good coverage!' },
                    { name: 'Fixed Network', content: 'Can be better for these _reasons_...' },
                ]
            },
        ],
    }, {
        id: '2',
        author: '1',
        name: 'How to Make a Sandwich',
        summary: 'You are probably hungry, _right_?',
        engagement: { locations: [], areasOfInterest: ['Cooking', 'Eating', 'Food'], focuses: [], backgrounds: [] },
        guidances: [
            {
                content: 'First, choose your bread.',
                options: [
                    { name: 'Whole wheat', content: 'A true classic!' },
                    { name: 'Pita', content: 'An _interesting_ choice.' },
                    { name: 'Rye', content: `Here's a pic: ![Rye bread](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Dark_rye_bread.JPG/1280px-Dark_rye_bread.JPG)` },
                ],
            },
            {
                content: 'Choose your peanut butter type',
                options: [
                    { name: 'Smooth', content: 'Smooth peanut butter!' },
                    { name: 'Crunchy', content: 'Crunchy peanut butter!' }
                ],
            }, {
                content: 'Choose your jelly type',
                options: [
                    { name: 'Strawberry', content: 'Strawberry!' },
                    { name: 'Raspberry', content: 'Raspberry!' }
                ]
            }
        ],
    }
];