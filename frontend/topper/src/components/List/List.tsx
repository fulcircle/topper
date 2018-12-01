import React, {Component} from 'react';
import './List.scss';
import ListItem from "./ListItem/ListItem";
import {Story} from "../../data/story.interface";
import {Link} from "react-router-dom";

interface Props {
    stories: any;
    filter: string;
    services: string[];
}

class List extends Component<Props> {

    constructor(props: Props) {
        super(props);
    }

    topStories(): Story[] {

        let stories: Story[] = [];
        for (let i = 0; i < 3; i++) {
            this.props.services.forEach(service => {
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

    camelCaseToSentence(txt: string) {
        let result = txt.replace( /([A-Z])/g, " $1" );
        return result.charAt(0).toUpperCase() + result.slice(1);
    }

    getFilterNode(service: string, idx: number) {
        if (this.props.filter === service || (this.props.filter=='topStories' && service==='All')) {
            return (<div key={idx} className="Filter">{this.camelCaseToSentence(service)}</div>)
        } else {
            return (<div key={idx} className="Filter">
                <Link to={service === 'All' ? '' : service}>{this.camelCaseToSentence(service)}</Link>
            </div>)
        }
    }

    render() {
        let mql = window.matchMedia("only screen and (min-device-width: 320px) and (max-device-width: 768px)");
        let nodes: React.ReactNode[] = [];
        let serviceNodes: React.ReactNode[] = [];
        let stories: Story[] = [];

        if (this.props.filter === 'topStories') {
            stories = this.topStories();
        } else {
            stories = this.storiesByService(this.props.filter);
        }

        stories.forEach((s: Story) => nodes.push(<ListItem truncate={mql.matches} key={s.id} story={s}/>));

        serviceNodes.push(this.getFilterNode('All', 0));

        this.props.services.forEach(( service, idx) => serviceNodes.push(
            this.getFilterNode(service, idx+1)
        ));

        return (
            // Title
            <div className="List">
                <div className="ListTitleHeading">
                    <div className="Headline">
                        <div className="ListTitlePadding" />
                        <div className="ListTitle">
                            topper
                        </div>
                    </div>
                    <div className="Headline">
                        <div className="ListTitlePadding" />
                        <div className="Filters">
                            {serviceNodes}
                        </div>
                    </div>
                </div>

                {nodes}

                {/* Footer */}
                <div className="ListTitleHeading">
                    <div className="Headline">
                    </div>
                </div>
            </div>
        );
    }
}

export default List;
