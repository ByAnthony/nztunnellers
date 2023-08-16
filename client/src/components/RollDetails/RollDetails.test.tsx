import '@testing-library/jest-dom';
import { screen } from '@testing-library/react';

import { mockDetailsList } from '../../utils/mocks/mockRoll';
import { renderWithMemoryRouter } from '../../utils/test-utils';

import { RollDetails } from './RollDetails';

const component = <RollDetails listOfTunnellers={mockDetailsList} />;

test('renders the component correctly', () => {
  const { asFragment } = renderWithMemoryRouter(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders details', () => {
  renderWithMemoryRouter(component);

  expect(screen.getByText('John')).toBeInTheDocument();
  expect(screen.getByText('Doe')).toBeInTheDocument();
  expect(screen.getByRole('link', { name: 'John Doe 1886-1952 →' }).getAttribute('href')).toBe('/tunnellers/26');

  expect(screen.getByText('Alexander')).toBeInTheDocument();
  expect(screen.getByText('Driscott')).toBeInTheDocument();
  expect(screen.getByRole('link', { name: 'Alexander Driscott 1886-1952 →' }).getAttribute('href')).toBe('/tunnellers/1');
});
