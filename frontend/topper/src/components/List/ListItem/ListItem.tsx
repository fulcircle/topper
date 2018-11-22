import React, { Component } from 'react';
import './ListItem.scss';
import {Story} from "../../../data/story.class";

interface Props {
    story: Story;
}

class ListItem extends Component<Props> {
    constructor(props: Props) {
        super(props);
    }

    render() {
        return (
            <div className="ListItem">
                {this.props.story.title}
            </div>
        );
    }
}

export default ListItem;
