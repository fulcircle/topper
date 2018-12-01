import React, { Component } from 'react';
import './ListItem.scss';
import {Story} from "../../../data/story.interface";
import moment from 'moment';
import camelCase from "camelcase";
import {Link} from "react-router-dom";

interface Props {
    truncate: boolean;
    story: Story;
}

class ListItem extends Component<Props> {
    constructor(props: Props) {
        super(props);
    }

    truncateText(txt: string, n:number, useWordBoundary=true) {
        if (txt.length <= n) { return txt; }
        let subString = txt.substr(0, n-1);
        return (useWordBoundary
            ? subString.substr(0, subString.lastIndexOf(' '))
            : subString) + "...";
    }


    render() {
        let service_file = "images/" + this.props.story.service.name.toLowerCase().replace(" ", "_") + ".jpg";
        let human_date = moment.utc(this.props.story.story_date).fromNow();

        let title = this.props.story.title;
        if (this.props.truncate) {
            title = this.truncateText(title, 75);
        }

        if (title === null || title === "") {
            title = "Untitled";
        }

        return (
            <div className="ListItem">
                <div className="Headline">
                    <div className="Service">
                        <Link to={camelCase(this.props.story.service.name)}><img alt={this.props.story.service.name} src={service_file} height="100%"/></Link>
                    </div>
                    <div className="Title">
                        <a target="_blank" href={this.props.story.url}>{title}</a>
                    </div>
                </div>
                <div className="Details">
                    {this.props.story.category !== 'default' &&
                    <div className="Category">
                        from&nbsp;
                        {this.props.story.service.name === "Reddit" &&
                        <span>/r/</span>}
                        {this.props.story.category}
                    </div>}
                    {this.props.story.comments !== null && <div className="Comments">
                        <a target="_blank" href={this.props.story.comments_url}>{this.props.story.comments + " comments"}</a>
                    </div>}
                    <div className="Date">
                        {human_date}
                    </div>
                </div>
            </div>
        );
    }
}

export default ListItem;
