import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-responsive-demo',
  templateUrl: './responsive-demo.component.html',
  styleUrls: ['./responsive-demo.component.css']
})
export class ResponsiveDemoComponent implements OnInit {
  name = 'World';

  constructor(private route: ActivatedRoute) {
    console.log('hello world!');
  }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      if (!!params['name']) {
        this.name = String(params['name']).toUpperCase();
      }
    });
  }

}
