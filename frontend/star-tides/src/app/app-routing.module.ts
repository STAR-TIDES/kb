import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ResponsiveDemoComponent } from './responsive-demo/responsive-demo.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'responsive-demo', component: ResponsiveDemoComponent },
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: '*', component: HomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
