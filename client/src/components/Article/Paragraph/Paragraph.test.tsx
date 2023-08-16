import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { mockSection } from '../../../utils/mocks/mockArticle';
import { Paragraph } from './Paragraph';

const component = (
  <Paragraph section={mockSection} />
);

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders title correctly', () => {
  render(component);

  expect(screen.getByText(/Section Title/)).toBeInTheDocument();
  expect(screen.getByRole('link')).toHaveAttribute('href', '#footnote_1');
  expect(screen.getByRole('link')).toHaveAttribute('id', 'reference_1');
});
