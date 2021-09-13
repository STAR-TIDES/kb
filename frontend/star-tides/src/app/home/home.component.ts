import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  searchControl = new FormControl('');

  ngOnInit() {
    this.searchControl.statusChanges.subscribe((data) => {
      console.log(data, this.searchControl.value);
    });
  }

  onSubmit() {
    console.log(`SUBMIT! ${this.searchControl.value}`);
  }
}
