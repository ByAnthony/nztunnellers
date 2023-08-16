import '@testing-library/jest-dom';
import {
  fireEvent, render, screen,
} from '@testing-library/react';

import { Footer } from './Footer';

const component = <Footer />;

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('can scroll to top of the page', () => {
  global.scrollTo = jest.fn();

  render(component);
  fireEvent.click(screen.getByRole('button'));

  expect(global.scrollTo).toHaveBeenCalledWith(0, 0);
});
