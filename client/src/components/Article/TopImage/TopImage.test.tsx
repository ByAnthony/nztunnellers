import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { mockImage } from '../../../utils/mocks/mockArticle';
import { TopImage } from './TopImage';

const component = (
  <TopImage image={mockImage} />
);

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders image correctly', () => {
  render(component);

  expect(screen.getByRole('img').getAttribute('src')).toEqual('/images/history/img-123.png');
  expect(screen.getByRole('img').getAttribute('alt')).toEqual('Accessible alt text');
});
