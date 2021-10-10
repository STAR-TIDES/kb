import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-guide-detail',
  templateUrl: './guide-detail.component.html',
  styleUrls: ['./guide-detail.component.css']
})
export class GuideDetailComponent implements OnInit {
  content = 'Some awesome *markdown* content!';

  constructor() { }

  ngOnInit(): void {
  }

}
