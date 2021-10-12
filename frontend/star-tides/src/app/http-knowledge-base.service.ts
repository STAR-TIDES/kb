import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Contact } from './data/contact';
import { KnowledgeBaseService } from './knowledge-base-service';
import { Project } from './data/project';
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
    return this.httpClient.post<Contact>(`
    ${environment.apiEndpoint}/contacts/`, JSON.stringify(contact), this.defaultEditorOptions());
  }
  updateProject(id: string, payload: Project): Observable<Project> {
    return this.httpClient.put<Project>(
      `${environment.apiEndpoint}/projects/${id}`, JSON.stringify(payload), this.defaultEditorOptions());
  }
  deleteProject(id: string): Observable<{}> {
    return this.httpClient.delete(`${environment.apiEndpoint}/projects/${id}`, this.defaultEditorOptions());
  }
  createProject(project: Project): Observable<Project> {
    return this.httpClient.post<Project>(
      `${environment.apiEndpoint}/projects/`, JSON.stringify(project), this.defaultEditorOptions());
  }
  getGuide(id: string): Observable<Guide> {
    return this.httpClient.get<Guide>(`${environment.apiEndpoint}/guides/${id}`);
  }
  listGuides(query?: string, pageToken?: string, pageSize?: number): Observable<Guide[]> {
    return this.httpClient.get<Guide[]>(`${environment.apiEndpoint}/guides/`);
  }
  updateGuide(id: string, guide: Guide): Observable<Guide> {
    return this.httpClient.put<Guide>(
      `${environment.apiEndpoint}/guides/${id}`, JSON.stringify(guide), this.defaultEditorOptions());
  }
  deleteGuide(id: string): Observable<{}> {
    return this.httpClient.delete(`${environment.apiEndpoint}/guides/${id}`, this.defaultEditorOptions());
  }
  createGuide(guide: Guide): Observable<Guide> {
    return this.httpClient.post<Guide>(`${environment.apiEndpoint}/guides/`, JSON.stringify(guide), this.defaultEditorOptions());
  }

  getContact(id: string): Observable<Contact> {
    return this.httpClient.get<Contact>(`${environment.apiEndpoint}/contacts/${id}`);
  }

  listContacts(query = '', pageToken = '', pageSize = 10): Observable<Contact[]> {
    return this.httpClient.get<Contact[]>(`${environment.apiEndpoint}/contacts/`);
  }

  updateContact(id: string, contact: Contact): Observable<Contact> {
    return this.httpClient.put<Contact>(
      `${environment.apiEndpoint}/contacts/${id}`, JSON.stringify(contact), this.defaultEditorOptions());
  }

  deleteContact(id: string): Observable<{}> {
    return this.httpClient.delete(`${environment.apiEndpoint}/contacts/${id}`, this.defaultEditorOptions());
  }

  getProject(id: string): Observable<Project> {
    return this.httpClient.get<Project>(`${environment.apiEndpoint}/projects/${id}`);
  }

  listProjects(query = '', pageToken = '', pageSize = 10): Observable<Project[]> {
    return this.httpClient.get<Project[]>(`${environment.apiEndpoint}/projects/`);
  }

  private getEditorCookie() {
    const cookie = this.document.cookie.split(';').find(c => c.trim().startsWith(this.EDITOR_COOKIE));
    if (!cookie) {
      return null;
    }
    return cookie.trim().substring((this.EDITOR_COOKIE + '=').length).trim();
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

  private defaultEditorOptions() {
    return {
      headers: this.authHeader(),
      withCredentials: true,
    };
  }
}
