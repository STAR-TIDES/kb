import { Observable, of } from "rxjs";
import { Contact } from "./data/contact";
import { KnowledgeBaseInterface } from "./knowledge-base-service-interface";

export class FakeKnowledgeBaseService implements KnowledgeBaseInterface {
    getContact(id: string): Observable<Contact> {
        throw new Error("Method not implemented.");
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
    contacts: Contact[] = [];
}