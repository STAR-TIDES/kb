import { Observable, of, throwError } from "rxjs";
import { Contact } from "./data/contact";
import { Project } from "./data/project";
import { KnowledgeBaseInterface } from "./knowledge-base-service-interface";

export class FakeKnowledgeBaseService implements KnowledgeBaseInterface {
    getContact(id: string): Observable<Contact> {
        const contact = this.contacts.find(c => c.id == id);
        return contact ? of(contact) : throwError(`contact ${id} not found`);
    }
    listContacts(query?: string, pageToken?: string, pageSize?: number): Observable<Contact[]> {
        return of(this.contacts);
    }
    updateContact(id: string, payload: Contact): Observable<Contact> {
        throw new Error("Method not implemented.");
    }
    deleteContact(id: string): Observable<{}> {
        throw new Error("Method not implemented.");
    }

    getProject(id: string) {
        const project = this.projects.find(p => p.id == id);
        return project ? of(project) : throwError(`project ${id} not found`)
    }

    listProjects(query?: string, pageToken?: string, pageSize?: number) {
        return of(this.projects);
    }

    contacts: Contact[] = [];
    projects: Project[] = [];
}