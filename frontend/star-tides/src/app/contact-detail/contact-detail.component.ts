import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { throwError } from 'rxjs';
import { switchMap } from 'rxjs/operators';
import { Availability } from '../data/availability';
import { Contact } from '../data/contact';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-contact-detail',
  templateUrl: './contact-detail.component.html',
  styleUrls: ['./contact-detail.component.css']
})
export class ContactDetailComponent implements OnInit {
  contact?: Contact;

  constructor(
    private activatedRoute: ActivatedRoute,
    private router: Router,
    private client: KnowledgeBaseService) { }

  ngOnInit(): void {
    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      console.error('id not present in route');
      this.router.navigate(['/contacts']);
    }

    this.client.getContact(id!).subscribe(
      contact => this.contact = contact,
      err => console.error(err));
  }

  contactIsAvailable(): boolean {
    return this.contact?.availability == Availability.Available;
  }
}
