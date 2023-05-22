import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { testId } from '../../utils/mocks/mockTunneller';
import { testSummary } from '../../utils/mocks/mockSummary';
import { ProfileHowToCite } from './ProfileHowToCite';

const mockToday = new Date('2023-05-04');
const component = <ProfileHowToCite id={testId} summary={testSummary} date={mockToday} />;

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders the title correctly', () => {
  render(component);

  expect(screen.getByText('How to cite this page')).toBeVisible();
});

test('renders the name and birth/death dates correctly', () => {
  render(component);

  expect(screen.getByTestId('howtocite')).toHaveTextContent('"John Doe (1888-1975)"');
});

test('renders the url with correct id', () => {
  render(component);

  expect(screen.getByTestId('howtocite')).toHaveTextContent('www.nztunnellers.com/tunnellers/26');
});
