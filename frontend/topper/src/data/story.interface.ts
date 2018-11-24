import {Service} from "./service.interface";

export interface Story {
    id: number;
    service: Service;
    title: string;
    url: string;
    content: string;
    comments: string;
    comments_url: string;
    score: string;
    date: Date;
    story_date: Date;
    status: string;
    top_ten: boolean;
    description: string;

    category: string;

    // Podcast
    podcastId: string;
    duration: number;
}