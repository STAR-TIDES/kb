import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ResponsiveDemoComponent } from './responsive-demo/responsive-demo.component';

const routes: Routes = [
  {path: 'responsive-demo', component: ResponsiveDemoComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
