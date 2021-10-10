import { Pipe, PipeTransform } from '@angular/core';

/** Pipe to render Markdown content.
 * 
 * Inspired by https://markrabey.com/2019/05/31/angular-markdown-pipe/.
 */
@Pipe({
  name: 'markdown'
})
export class MarkdownPipe implements PipeTransform {

  transform(value: unknown, ...args: unknown[]): unknown {
    return null;
  }

}
