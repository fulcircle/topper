import React, {Component} from 'react';
import './List.scss';
import ListItem from "./ListItem/ListItem";
import {Story} from "../../data/story.interface";

interface Props {
    stories: any;
    filter: string;
}

class List extends Component<Props> {

    constructor(props: Props) {
        super(props);
    }

    topStories(): Story[] {

        let stories: Story[] = [];
        for (let i = 0; i < 3; i++) {
            Object.keys(this.props.stories).forEach(service => {
                Object.keys(this.props.stories[service]).forEach(category => {

                    let matches: Story[] =
                        this.props.stories[service][category].filter((s: Story) => stories.indexOf(s) == -1);

                    if (matches.length > 0) {
                        if (category === 'default') {
                            for (let i = 0; i < 3; i++) {
                                if (i < matches.length) {
                                    stories.push(matches[i])
                                }
                            }
                        } else {
                            stories.push(matches[0]);
                        }
                    }
                })
            });
        }

        return stories;

    }

    storiesByService(service: string) {
        let stories: Story[] = [];
        if (this.props.stories.hasOwnProperty(service)) {
            Object.keys(this.props.stories[service]).forEach((category: string) => {
                this.props.stories[service][category].forEach((story: Story) => {
                    stories.push(story)
                })
            });
        }

        return stories;
    }

    render() {
        let mql = window.matchMedia("only screen and (min-device-width: 320px) and (max-device-width: 768px)");
        let nodes: React.ReactNode[] = [];
        let stories: Story[] = [];

        if (this.props.filter === 'topStories') {
            stories = this.topStories();
        } else {
            stories = this.storiesByService(this.props.filter);
        }

        stories.forEach((s: Story) => nodes.push(<ListItem truncate={mql.matches} key={s.id} story={s}/>));

        return (
            <div className="List">
                {nodes}
            </div>
        );
    }
}

export default List;
