import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Guide } from '../data/guide';
import { KnowledgeBaseService } from '../knowledge-base-service';

@Component({
  selector: 'app-guide-edit',
  templateUrl: './guide-edit.component.html',
  styleUrls: ['./guide-edit.component.css']
})
export class GuideEditComponent implements OnInit {
  guide?: Guide;
  isNew = false;

  constructor(
    private activatedRoute: ActivatedRoute,
    private service: KnowledgeBaseService,
    private router: Router,
  ) { }

  ngOnInit(): void {
    const isNew = this.router.url.includes('/new');
    if (isNew) {
      this.isNew = true;
      this.guide = {
        id: '',
        name: '',
        author: '',
        summary: '',
        engagement: {
          locations: [],
          areasOfInterest: [],
          backgrounds: [],
          focuses: [],
        },
        guidances: [],
      };
      return;
    }

    const id = this.activatedRoute.snapshot.paramMap.get('id');
    if (!id) {
      console.error('id not present in route');
      this.router.navigate(['/guides']);
      return;
    }

    this.service.getGuide(id).subscribe(g => this.guide = g);
  }

  onDeleteClick() {
    if (!this.guide) {
      throw new Error('expected guide to be present');
    }

    this.service.deleteGuide(this.guide.id).subscribe(_ => this.router.navigate(['/guides']));
  }

  onUpdateClick() {
    if (!this.guide) {
      throw new Error('expected guide to be present');
    }

    this.service.updateGuide(this.guide.id, this.guide)
      .subscribe(g => this.router.navigate(['/guides', g.id]));
  }

  onCreateClick() {
    this.service.createGuide(this.guide!!)
      .subscribe(g => this.router.navigate(['/guides', g.id]));
  }
}
