import React, {Component} from 'react';
import './List.scss';
import {Story} from "../../data/story.interface";
import ListItem from "./ListItem/ListItem";

interface Props {
    stories: Story[];
}

class List extends Component<Props> {
    constructor(props: Props) {
        super(props);
    }

    render() {
        const stories: React.ReactNode[] = this.props.stories.map((story) => {
            return <ListItem key={story.id} story={story}/>
        });

        return (
            <div className="List">
                {stories}
            </div>
        );
    }
}

export default List;
