import React, {Component} from 'react';
import './List.scss';
import ListItem from "./ListItem/ListItem";
import {Story} from "../../data/story.interface";

interface Props {
    stories: any;
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

    render() {
        let stories: React.ReactNode[] = [];
        let topStories = this.topStories();

        topStories.forEach((s: Story) => stories.push(<ListItem key={s.id} story={s}/>));

        return (
            <div className="List">
                {stories}
            </div>
        );
    }
}

export default List;
