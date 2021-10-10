import { TestBed } from '@angular/core/testing';

import { HttpKnowledgeBaseService as HttpKnowledgeBaseService } from './http-knowledge-base.service';

describe('HttpKnowledgeBaseService', () => {
  let service: HttpKnowledgeBaseService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HttpKnowledgeBaseService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
