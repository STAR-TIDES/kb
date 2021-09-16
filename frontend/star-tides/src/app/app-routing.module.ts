import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContactDetailComponent } from './contact-detail/contact-detail.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { GuideDetailComponent } from './guide-detail/guide-detail.component';
import { GuideListComponent } from './guide-list/guide-list.component';
import { HomeComponent } from './home/home.component';
import { ProjectDetailComponent } from './project-detail/project-detail.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { ResponsiveDemoComponent } from './responsive-demo/responsive-demo.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'responsive-demo', component: ResponsiveDemoComponent },
  { path: 'contacts/:id', component: ContactDetailComponent },
  { path: 'contacts', component: ContactListComponent },
  { path: 'projects/:id', component: ProjectDetailComponent },
  { path: 'projects', component: ProjectListComponent },
  { path: 'guides', component: GuideListComponent },
  { path: 'guides/:id', component: GuideDetailComponent },
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: '*', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
