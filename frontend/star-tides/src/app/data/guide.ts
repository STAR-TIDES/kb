import { Engagement } from "./engagement";

export interface Guide {
    id: string;
    name: string;
    summary: string;
    author: string;
    relatedProjects?: string[];
    relevantContacts?: string[];
    engagement: Engagement;
    guidances?: Guidance[];
};

export interface Guidance {
    content: string;
    options?: GuidanceOption[];
};

export interface GuidanceOption {
    name: string;
    content: string;
};