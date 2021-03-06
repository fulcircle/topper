import {Story} from "../data/story.interface";

export class Api {

    static getStories(): Promise<Story[]> {
        return fetch('/api/story')
            .then(response => {
                if (!response.ok) {
                    throw new Error(response.statusText)
                }
                return response.json().then(data => data.objects as Story[])
            })

    }
}
