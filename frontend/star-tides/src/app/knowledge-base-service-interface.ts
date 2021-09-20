import { Observable } from "rxjs";
import { Contact } from "./data/contact";
import { Project } from "./data/project";

export interface KnowledgeBaseInterface {
    getContact(id: string): Observable<Contact>;
    listContacts(query?: string, pageToken?: string, pageSize?: number): Observable<Contact[]>;
    updateContact(id: string, payload: Contact): Observable<Contact>;
    deleteContact(id: string): Observable<{}>;

    getProject(id: string): Observable<Project>;
    listProject(query?: string, pageToken?: string, pageSize?: number): Observable<Project[]>;
}