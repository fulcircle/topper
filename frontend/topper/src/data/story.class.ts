export interface Story {
    id: number;
    service: string;
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

    // Reddit
    subreddit: string;

    // Podcast
    podcastId: string;
    duration: string;
}