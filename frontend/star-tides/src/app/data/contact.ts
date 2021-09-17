import { Availability } from "./availability";
import { Engagement } from "./engagement";
import { Location } from "./location";

export interface Contact {
    name: String;
    location: Location;
    availability: Availability;
    id: String;
    userId?: String;
    email?: String;
    phoneNumber?: String;
    jobTitle?: String;
    websiteURL?: String;
    languages: String[];
    statuses: String[];
    engagement: Engagement;
}