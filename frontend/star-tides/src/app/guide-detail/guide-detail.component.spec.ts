import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GuideDetailComponent } from './guide-detail.component';

describe('GuideDetailComponent', () => {
  let component: GuideDetailComponent;
  let fixture: ComponentFixture<GuideDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GuideDetailComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GuideDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
