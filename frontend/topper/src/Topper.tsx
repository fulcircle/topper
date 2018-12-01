import React, {Component} from 'react';
import './Topper.scss';
import List from "./components/List/List";
import {Story} from "./data/story.interface";
import {Api} from "./services/api.class";
import camelCase from 'camelcase';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import ScrollToTop from "./components/ScrollToTop/ScrollToTop";
import Spinner from "./components/Spinner/Spinner";

interface State {
    stories: any;
    services: string[];
    loading: boolean;
}

interface Props {

}

class Topper extends Component<Props, State> {

    constructor(props: Props) {
        super(props);
        this.state = {stories: {}, services: [], loading: false};
    }
    componentDidMount(): void {
        this.setState({loading: true});
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
            this.setState({stories: stories, services: Object.keys(stories), loading: false})
        })
    }

    render() {
        let nodes: React.ReactNode[] = [];

        this.state.services.forEach((service, idx) => {
            nodes.push(
                <Route key={idx+1} exact path={'/' + service}>
                    <List stories={this.state.stories} services={this.state.services} filter={service}/>
                </Route>);
        });

        nodes.push(
            <Route key="0">
                <List stories={this.state.stories} services={this.state.services} filter='topStories'/>
            </Route>
        );

        let spinner = this.state.loading ? (
            <div className="spinner">
                <Spinner/>
            </div>
        ) : null;

        let app = (
            <div className="Topper" style={{opacity: this.state.loading ? 0 : 1}}>
                <Switch>
                    {nodes}
                </Switch>
            </div>
        );


        return (
            <Router>
                <ScrollToTop>
                    {spinner}
                    {app}
                </ScrollToTop>
            </Router>
        );
    }
}

export default Topper;
