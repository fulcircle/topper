import React, {Component} from 'react';
import './Topper.scss';
import List from "./components/List/List";
import {Story} from "./data/story.class";
import {Api} from "./services/api.class";

interface State {
    stories: Story[]
}

interface Props {

}

class Topper extends Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {stories: []};
    }
    componentDidMount(): void {
        Api.getStories().then((data: Story[]) => {
            this.setState({stories: data})
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
