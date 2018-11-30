import React, {Component} from 'react';
import './Topper.scss';
import List from "./components/List/List";
import {Story} from "./data/story.interface";
import {Api} from "./services/api.class";
import camelCase from 'camelcase';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';

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

                /* By setting podcast category to 'default', we can display titles from *all podcasts*
                as a single group (rather than separating by each podcast category) together on the top stories timeline */
                if (service === 'pocketcasts') {
                    category = 'default'
                }

                !(service in stories) && (stories[service] = []);
                !(category in stories[service]) && (stories[service][category] = []);
                stories[service][category].push(story)

            });
            this.setState({stories: stories})
        })
    }

    render() {
        let nodes: React.ReactNode[] = [];

        let key = 0;

        Object.keys(this.state.stories).forEach((service: string) => {
            nodes.push(
                <Route key={key} exact path={'/' + service}>
                    <List stories={this.state.stories} filter={service}/>
                </Route>);
            key += 1;
        });

        nodes.push(
            <Route key={key}>
                <List stories={this.state.stories} filter='topStories'/>
            </Route>
        );


        return (
            <Router>
                <div className="Topper">
                    <Switch>
                        {nodes}
                    </Switch>
                </div>
            </Router>
        );
    }
}

export default Topper;
