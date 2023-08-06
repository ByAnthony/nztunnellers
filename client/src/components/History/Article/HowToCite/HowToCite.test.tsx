import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { mockToday } from '../../../../utils/mocks/mockToday';
import { mockTitle } from '../../../../utils/mocks/mockArticle';
import { HowToCite } from './HowToCite';

const component = (
  <HowToCite title={mockTitle} today={mockToday} />
);

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders next chapter button correctly', () => {
  render(component);

  expect(screen.getByText(/How to cite this page/)).toBeInTheDocument();
  expect(screen.getByText(/My Awesome Article Title/)).toBeInTheDocument();
  expect(screen.getByText(/4 May 2023/)).toBeInTheDocument();
});
