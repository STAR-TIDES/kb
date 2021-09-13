import { Component } from '@angular/core';
import { MatDrawer } from '@angular/material/sidenav';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'star-tides';
  name = 'World';

  drawerClick(drawer: MatDrawer) {
    console.log(drawer);
    drawer.toggle();
  }

  // constructor(private route: ActivatedRoute) {}

  // ngOnInit() {
  //   this.route.queryParams.subscribe(params => {
  //     if (!!params['name']) {
  //       this.name = params['name'];
  //     }
  //   });
  // }
}
