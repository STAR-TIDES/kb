import { Observable } from "rxjs";
import { Contact } from "./data/contact";

export interface KnowledgeBaseInterface {
    getContact(id: string): Observable<Contact>;
    listContacts(query?: string, pageToken?: string, pageSize?: number): Observable<Contact[]>;
    updateContact(id: string, payload: Contact): Observable<Contact>;
    deleteContact(id: string): Observable<{}>;
}