import React from 'react';
import ReactDOM from 'react-dom';
import Topper from './Topper';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<Topper />, div);
  ReactDOM.unmountComponentAtNode(div);
});
