import { ValueProvider } from "@angular/core";
import { ActivatedRoute, ParamMap, Params } from "@angular/router";
import { Observable, of } from "rxjs";

export class FakeActivatedRouteProvider implements ValueProvider {
    private paramMap: ParamMap = (new Map()) as unknown as ParamMap;

    useValue = { snapshot: { paramMap: this.paramMap } };
    provide = ActivatedRoute;

    setParamMap(paramMap: ParamMap) {
        this.paramMap = paramMap;
    }
}