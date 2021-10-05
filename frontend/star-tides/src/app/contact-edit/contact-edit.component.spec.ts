import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ALL_APP_ROUTES } from '../app-routing.module';
import { FakeActivatedRouteProvider } from '../fake-activated-route';

import { ContactEditComponent } from './contact-edit.component';

describe('ContactEditComponent', () => {
  let component: ContactEditComponent;
  let fixture: ComponentFixture<ContactEditComponent>;
  let activatedRoute = new FakeActivatedRouteProvider();

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RouterTestingModule.withRoutes(ALL_APP_ROUTES)],
      declarations: [ContactEditComponent],
      providers: [activatedRoute],
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ContactEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
