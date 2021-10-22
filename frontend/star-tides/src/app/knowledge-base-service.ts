import { Observable } from "rxjs";
import { Contact } from "./data/contact";
import { Guide } from "./data/guide";
import { Project } from "./data/project";

export abstract class KnowledgeBaseService {
    abstract getContact(id: string): Observable<Contact>;
    abstract listContacts(query?: string, pageToken?: string, pageSize?: number): Observable<Contact[]>;
    abstract updateContact(id: string, payload: Contact): Observable<Contact>;
    abstract deleteContact(id: string): Observable<{}>;
    abstract createContact(contact: Contact): Observable<Contact>;

    abstract getProject(id: string): Observable<Project>;
    abstract listProjects(query?: string, pageToken?: string, pageSize?: number): Observable<Project[]>;
    abstract updateProject(id: string, payload: Project): Observable<Project>;
    abstract deleteProject(id: string): Observable<{}>;
    abstract createProject(project: Project): Observable<Project>;

    abstract getGuide(id: string): Observable<Guide>;
    abstract listGuides(query?: string, pageToken?: string, pageSize?: number): Observable<Guide[]>;
    abstract updateGuide(id: string, guide: Guide): Observable<Guide>;
    abstract deleteGuide(id: string): Observable<{}>;
    abstract createGuide(guide: Guide): Observable<Guide>;
}