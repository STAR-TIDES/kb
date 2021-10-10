import { Injectable } from '@angular/core';
import { Observable, of, throwError } from 'rxjs';
import { Contact } from './data/contact';
import { KnowledgeBaseService } from './knowledge-base-service';
import { Project, ProjectStatus } from './data/project';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Guide } from './data/guide';

@Injectable({
  providedIn: 'root'
})
export class HttpKnowledgeBaseService extends KnowledgeBaseService {
  private readonly EDITOR_COOKIE = 'StarTidesEditor';

  constructor(private httpClient: HttpClient, private document: Document) {
    super();
  }

  createContact(contact: Contact): Observable<Contact> {
    throw new Error('Method not implemented.');
  }
  updateProject(id: string, payload: Project): Observable<Project> {
    throw new Error('Method not implemented.');
  }
  deleteProject(id: string): Observable<{}> {
    throw new Error('Method not implemented.');
  }
  createProject(project: Project): Observable<Project> {
    throw new Error('Method not implemented.');
  }
  getGuide(id: string): Observable<Guide> {
    throw new Error('Method not implemented.');
  }
  listGuides(query?: string, pageToken?: string, pageSize?: number): Observable<Guide[]> {
    throw new Error('Method not implemented.');
  }
  updateGuide(id: string, guide: Guide): Observable<Guide> {
    throw new Error('Method not implemented.');
  }
  deleteGuide(id: string): Observable<{}> {
    throw new Error('Method not implemented.');
  }
  createGuide(guide: Guide): Observable<Guide> {
    throw new Error('Method not implemented.');
  }

  private getEditorCookie() {
    const cookie = this.document.cookie.split(';').find(c => c.startsWith(this.EDITOR_COOKIE));
    if (!cookie) {
      return null;
    }
    return cookie.substring((this.EDITOR_COOKIE + '=').length);
  }

  private authHeader() {
    const cookie = this.getEditorCookie();
    if (!cookie) {
      throw new Error('editor cookie is not present');
    }
    return {
      'Authorization': `Bearer: ${cookie}`
    };
  }

  getContact(id: string): Observable<Contact> {
    return this.httpClient.get<Contact>(`${environment.apiEndpoint}/contacts/${id}`);
  }

  listContacts(query = '', pageToken = '', pageSize = 10): Observable<Contact[]> {
    return this.httpClient.get<Contact[]>(`${environment.apiEndpoint}/contacts/`);
  }

  updateContact(id: string, contact: Contact): Observable<Contact> {
    return this.httpClient.put<Contact>(`${environment.apiEndpoint}/contacts/${id}`, JSON.stringify(contact), {
      headers: this.authHeader(),
      withCredentials: true,
    });
  }

  deleteContact(id: string): Observable<{}> {
    return this.httpClient.delete(`${environment.apiEndpoint}/contacts/${id}`).pipe(() => of({}));
  }

  getProject(id: string): Observable<Project> {
    return this.httpClient.get<Project>(`${environment.apiEndpoint}/projects/${id}`);
  }

  listProjects(query = '', pageToken = '', pageSize = 10): Observable<Project[]> {
    return this.httpClient.get<Project[]>(`${environment.apiEndpoint}/projects/`);
  }
}
