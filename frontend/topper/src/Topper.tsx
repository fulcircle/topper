import React, {Component} from 'react';
import './Topper.scss';
import List from "./components/List/List";
import {Story} from "./data/story.interface";
import {Api} from "./services/api.class";
import camelCase from 'camelcase';

interface State {
    stories: any;
}

interface Props {

}

class Topper extends Component<Props, State> {

    constructor(props: Props) {
        super(props);
        this.state = {stories: {}};
    }
    componentDidMount(): void {
        Api.getStories().then((data: Story[]) => {
            let stories: any = {};
            data.forEach(story => {
                let category = camelCase(story.category);
                let service = camelCase(story.service.name);

                !(service in stories) && (stories[service] = []);
                !(category in stories[service]) && (stories[service][category] = []);
                stories[service][category].push(story)

            });
            this.setState({stories: stories})
        })
    }

    render() {
        return (
            <div className="Topper">
                <List stories={this.state.stories}/>
            </div>
        );
    }
}

export default Topper;
