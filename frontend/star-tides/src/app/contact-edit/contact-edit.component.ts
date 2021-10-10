import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Availability, AVAILABILITY_LIST } from '../data/availability';
import { Contact } from '../data/contact';
import { HttpKnowledgeBaseService } from '../http-knowledge-base.service';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-contact-edit',
  templateUrl: './contact-edit.component.html',
  styleUrls: ['./contact-edit.component.css']
})
export class ContactEditComponent implements OnInit {
  contact?: Contact;
  AVAILABILITY_LIST = AVAILABILITY_LIST;
  isNew: boolean = false;

  constructor(
    private activatedRoute: ActivatedRoute,
    private service: KnowledgeBaseService,
    private router: Router) { }

  ngOnInit(): void {
    console.log(this.activatedRoute.snapshot);
    const isNew = (this.activatedRoute.snapshot.routeConfig?.path || '').indexOf('/new') >= 0;
    if (isNew) {
      this.isNew = true;
      this.contact = {
        id: '',
        name: '',
        location: {
          iso31661CountryCode: 0,
          arbitraryText: '',
        },
        availability: Availability.Unavailable,
        languages: [],
        statuses: [],
        engagement: {
          locations: [],
          backgrounds: [],
          areasOfInterest: [],
          focuses: [],
        },
      };
      return;
    }

    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      console.error('contact id not present in route');
      this.router.navigate(['/contacts']);
      return;
    }

    this.service.getContact(id).subscribe(c => this.contact = c);
  }

  onDeleteClick() {
    if (!this.contact) {
      throw new Error('no contact');
    }

    this.service.deleteContact(this.contact.id).subscribe(
      _ => window.alert(`Successfully deleted ${this.contact?.name}!`));
  }

  onUpdateClick() {
    if (!this.contact) {
      throw new Error('no contact');
    }

    this.service.updateContact(this.contact.id, this.contact).subscribe(
      c => this.router.navigate(['/contacts', c.id]));
  }

  onCreateClick() {
    this.service.createContact(this.contact!!)
      .subscribe(c => this.router.navigate(['/contacts', c.id]));
  }
}
