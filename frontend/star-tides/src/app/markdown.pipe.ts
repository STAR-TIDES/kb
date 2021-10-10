import { Pipe, PipeTransform } from '@angular/core';
import * as marked from 'marked';

/** Pipe to render Markdown content.
 * 
 * Inspired by https://markrabey.com/2019/05/31/angular-markdown-pipe/.
 */
@Pipe({
  name: 'markdown'
})
export class MarkdownPipe implements PipeTransform {

  transform(value: unknown): any {
    const content = value as string;
    if (content.length < 1) {
      return '';
    }
    return marked(content);
  }

}
