import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { AVAILABILITY_LIST } from '../data/availability';
import { Contact } from '../data/contact';
import { KnowledgeBaseService } from '../knowledge-base.service';

@Component({
  selector: 'app-contact-edit',
  templateUrl: './contact-edit.component.html',
  styleUrls: ['./contact-edit.component.css']
})
export class ContactEditComponent implements OnInit {
  contact?: Contact;
  AVAILABILITY_LIST = AVAILABILITY_LIST;

  constructor(
    private activatedRoute: ActivatedRoute,
    private service: KnowledgeBaseService,
    private router: Router) { }

  ngOnInit(): void {
    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      throw new Error('id not present in route');
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
}
