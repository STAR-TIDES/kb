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

export class FakeParamMap implements ParamMap {
    has(name: string): boolean {
        throw new Error("Method not implemented.");
    }
    get(name: string): string | null {
        return this.map.get(name) || null;
    }
    getAll(name: string): string[] {
        throw new Error("Method not implemented.");
    }

    get keys() {
        return Object.keys(this.map);
    }

    constructor(private map: Map<string, string>) { }

}