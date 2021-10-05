import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ParamMap } from '@angular/router';
import { FakeActivatedRouteProvider, FakeParamMap } from '../fake-activated-route';

import { SearchResultsComponent } from './search-results.component';

describe('SearchResultsComponent', () => {
  let component: SearchResultsComponent;
  let fixture: ComponentFixture<SearchResultsComponent>;
  let activatedRoute = new FakeActivatedRouteProvider();

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SearchResultsComponent],
      providers: [activatedRoute],
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchResultsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    const paramMap = new Map();
    paramMap.set('id', 'abc123');
    activatedRoute.setParamMap(new FakeParamMap(paramMap));
    expect(component).toBeTruthy();
  });
});
