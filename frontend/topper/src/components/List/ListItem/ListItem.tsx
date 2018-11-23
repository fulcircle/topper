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
                <div className="Headline">
                    <div className="Service">
                        <img src={service_file} height="100%"/>
                    </div>
                    <div className="Title">
                        {this.props.story.title}
                    </div>
                </div>
                <div className="Details">
                    {this.props.story.service.name === "Reddit" &&
                    <div className="Category">
                        from /r/{this.props.story.subreddit}
                    </div>}
                    {this.props.story.service.name === "Pocketcasts" &&
                    <div className="Category">
                        from {this.props.story.description}
                    </div>}
                    {this.props.story.service.name !== "Pocketcasts" && <div className="Comments">
                        {this.props.story.comments + " comments"}
                    </div>}
                </div>
            </div>
        );
    }
}

export default ListItem;
