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
        let service_file = "/images/" + this.props.story.service.name.toLowerCase().replace(" ", "_") + ".jpg";
        return (
            <div className="ListItem">
                <div className="Category">
                    <img src={service_file} height="100%"/>
                </div>
                <div className="Info">
                    {this.props.story.title}
                </div>
            </div>
        );
    }
}

export default ListItem;
