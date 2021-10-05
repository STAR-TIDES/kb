import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ALL_APP_ROUTES } from '../app-routing.module';
import { FakeActivatedRouteProvider } from '../fake-activated-route';
import { FakeKnowledgeBaseService } from '../fake-knowledge-base-service';
import { KnowledgeBaseService } from '../knowledge-base.service';

import { ContactDetailComponent } from './contact-detail.component';

describe('ContactDetailComponent', () => {
  let component: ContactDetailComponent;
  let fixture: ComponentFixture<ContactDetailComponent>;
  let activatedRoute = new FakeActivatedRouteProvider();

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RouterTestingModule.withRoutes(ALL_APP_ROUTES)],
      declarations: [ContactDetailComponent],
      providers: [activatedRoute, { provide: KnowledgeBaseService, useClass: FakeKnowledgeBaseService }],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ContactDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
