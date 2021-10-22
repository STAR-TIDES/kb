import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { switchMap } from 'rxjs/operators';
import { Contact } from '../data/contact';
import { Guide } from '../data/guide';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-guide-detail',
  templateUrl: './guide-detail.component.html',
  styleUrls: ['./guide-detail.component.css']
})
export class GuideDetailComponent implements OnInit {
  guide?: Guide;
  author?: Contact;

  constructor(private activatedRoute: ActivatedRoute, private service: KnowledgeBaseService, private router: Router) { }

  ngOnInit(): void {
    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      console.error('id not present in route');
      this.router.navigate(['/guides']);
      return;
    }

    const obs = this.service.getGuide(id);
    obs.subscribe(g => this.guide = g);
    obs.pipe(switchMap(g => this.service.getContact(g.author)))
      .subscribe(c => this.author = c);
  }

}
