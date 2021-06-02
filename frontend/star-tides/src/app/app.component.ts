import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'star-tides';
  name = 'World';

  constructor(private route: ActivatedRoute) {
    console.log('reporting for duty!');
  }

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      if (!!params['name']) {
        this.name = params['name'];
      }
    });
  }
}
