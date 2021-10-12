import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContactDetailComponent } from './contact-detail/contact-detail.component';
import { ContactEditComponent } from './contact-edit/contact-edit.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { GuideDetailComponent } from './guide-detail/guide-detail.component';
import { GuideEditComponent } from './guide-edit/guide-edit.component';
import { GuideListComponent } from './guide-list/guide-list.component';
import { HomeComponent } from './home/home.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { ProjectDetailComponent } from './project-detail/project-detail.component';
import { ProjectEditComponent } from './project-edit/project-edit.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { SearchResultsComponent } from './search-results/search-results.component';

export const ALL_APP_ROUTES: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'contacts/new', component: ContactEditComponent },
  { path: 'contacts/:id/edit', component: ContactEditComponent },
  { path: 'contacts/:id', component: ContactDetailComponent },
  { path: 'contacts', component: ContactListComponent },
  { path: 'projects/new', component: ProjectEditComponent },
  { path: 'projects/:id/edit', component: ProjectEditComponent },
  { path: 'projects/:id', component: ProjectDetailComponent },
  { path: 'projects', component: ProjectListComponent },
  { path: 'guides/new', component: GuideEditComponent },
  { path: 'guides/:id', component: GuideDetailComponent },
  { path: 'guides/:id/edit', component: GuideEditComponent },
  { path: 'guides', component: GuideListComponent },
  { path: 'query', component: SearchResultsComponent },
  { path: 'query/:query', component: SearchResultsComponent },
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: '*', component: HomeComponent },
  { path: '**', component: PageNotFoundComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(ALL_APP_ROUTES)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
