import '@testing-library/jest-dom';
import { render } from '@testing-library/react';
import { mockId } from '../../utils/mocks/mockProfile';
import { mockSummary } from '../../utils/mocks/mockSummary';
import { ProfileHowToCite } from './ProfileHowToCite';
import { findElementWithText } from '../../utils/test-utils';

const mockToday = new Date('2023-05-04');
const component = <ProfileHowToCite id={mockId} summary={mockSummary()} date={mockToday} />;

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

describe('Name', () => {
  test('renders name correctly', () => {
    render(component);

    const element = findElementWithText('"John Doe (1888-1975)"');

    expect(element).toBeInTheDocument();
  });
});

describe('Dates', () => {
  test('renders birth and death dates when known', () => {
    render(component);

    const element = findElementWithText('"John Doe (1888-1975)"');

    expect(element).toBeInTheDocument();
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

    const element = findElementWithText('"John Doe (1888-†?)"');

    expect(element).toBeInTheDocument();
  });
});

describe('URL', () => {
  test('renders the url with correct id', () => {
    render(component);

    const element = findElementWithText('www.nztunnellers.com/tunnellers/26');

    expect(element).toBeInTheDocument();
  });
});
