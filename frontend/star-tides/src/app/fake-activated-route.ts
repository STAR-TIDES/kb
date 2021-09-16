import { ValueProvider } from "@angular/core";
import { ActivatedRoute, Params } from "@angular/router";
import { Observable, of } from "rxjs";

export class FakeActivatedRouteProvider implements ValueProvider {
    private queryParams: Observable<Params> = of();
    private params: Observable<Params> = of();

    useValue = { queryParams: this.queryParams, params: this.params };
    provide = ActivatedRoute;


    setQueryParams(queryParams: Observable<Params>) {
        this.queryParams = queryParams;
    }

    setParams(params: Observable<Params>) {
        this.params = params;
    }
}