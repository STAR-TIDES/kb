import { Component } from '@angular/core';
import { MatDrawer } from '@angular/material/sidenav';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  now = new Date();

  drawerClick(drawer: MatDrawer) {
    console.log(drawer);
    drawer.toggle();
  }
}
