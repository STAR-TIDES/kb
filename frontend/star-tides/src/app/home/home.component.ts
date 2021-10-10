import { Component, OnInit } from '@angular/core';
import { FormControl, NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {

  }
  onSubmit(searchForm: NgForm) {
    let query: string = searchForm.value?.search;
    if (!query) {
      query = '';
    }

    this.router.navigate(['/query', query]);
  }
}
