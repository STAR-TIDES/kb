import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { FakeKnowledgeBaseService } from '../fake-knowledge-base-service';
import { HttpKnowledgeBaseService } from '../http-knowledge-base.service';

import { ContactListComponent } from './contact-list.component';

describe('ContactListComponent', () => {
  let component: ContactListComponent;
  let fixture: ComponentFixture<ContactListComponent>;
  let fakeClient: FakeKnowledgeBaseService;


  beforeEach(async () => {
    fakeClient = new FakeKnowledgeBaseService();

    await TestBed.configureTestingModule({
      declarations: [ContactListComponent],
      providers: [{ provide: HttpKnowledgeBaseService, useValue: fakeClient }]
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ContactListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
