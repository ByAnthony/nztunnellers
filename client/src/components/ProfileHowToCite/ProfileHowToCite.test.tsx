import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { mockId } from '../../utils/mocks/mockProfile';
import { mockSummary } from '../../utils/mocks/mockSummary';
import { ProfileHowToCite } from './ProfileHowToCite';

const mockToday = new Date('2023-05-04');
const component = <ProfileHowToCite id={mockId} summary={mockSummary()} date={mockToday} />;

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders birth and death dates when known', () => {
  render(component);

  expect(screen.getByTestId('howtocite')).toHaveTextContent('"John Doe (1888-1975)"');
});

test('renders only birth date when death date unknown', () => {
  const componentWithoutDeathDate = (
    <ProfileHowToCite
      id={mockId}
      summary={mockSummary({ death: null })}
      date={mockToday}
    />
  );
  render(componentWithoutDeathDate);

  expect(screen.getByTestId('howtocite')).toHaveTextContent('"John Doe (1888-†?)"');
});

test('renders the url with correct id', () => {
  render(component);

  expect(screen.getByTestId('howtocite')).toHaveTextContent('www.nztunnellers.com/tunnellers/26');
});
