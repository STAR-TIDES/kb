import { ContactNameAndId } from "./contact";
import { Engagement } from "./engagement";
import { Location } from "./location";

export interface Project {
    id: string;
    name: string;
    location: Location;
    engagement: Engagement;
    contacts: ContactNameAndId[];
    summary: string;
    solutionCosts?: string;
    updates?: ProjectUpdate[];
    notes?: string;
    status: ProjectStatus;
}

export enum ProjectStatus {
    Unspecified = 'UNSPECIFIED',
    Proposed = 'PROPOSED',
    ProposedHelpWanted = 'PROPOSED_HELP_WANTED',
    InProgress = 'IN_PROGRESS',
    InProgressHelpWanted = 'IN_PROGRESS_HELP_WANTED',
    Abandoned = 'ABANDONED',
    Completed = 'COMPLETED'
}
export interface ProjectUpdate {
    timestamp: Date,
    userId: string,
    content: string,
    requestingContactId?: string,
}