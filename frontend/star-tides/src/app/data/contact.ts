import { Availability } from "./availability";
import { Engagement } from "./engagement";
import { Location } from "./location";

export interface Contact {
    name: string;
    location: Location;
    availability: Availability;
    id: string;
    userId?: string;
    email?: string;
    phoneNumber?: string;
    jobTitle?: string;
    websiteURL?: string;
    languages: string[];
    statuses: string[];
    engagement: Engagement;
}

export interface ContactNameAndId {
    id?: string;
    name: string;
}