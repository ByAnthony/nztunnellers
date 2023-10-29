import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';

import { findElementWithText } from '../../utils/test';
import { mockId } from '../../utils/mocks/mockProfile';
import { mockSummary } from '../../utils/mocks/mockSummary';
import { mockTitle } from '../../utils/mocks/mockArticle';
import { mockToday } from '../../utils/mocks/mockToday';

import { HowToCite, HowToCiteTitle, HowToCiteUrl } from './HowToCite';

describe('HowToCiteUrl', () => {
  test('renders url for a specific tunneller', () => {
    render(<HowToCiteUrl id={26} title={undefined} timeline={false} />);
    expect(screen.getByText(/URL: www.nztunnellers.com\/tunnellers\/26/)).toBeInTheDocument();
  });

  test('renders url for a specific tunneller timeline', () => {
    render(<HowToCiteUrl id={26} title={undefined} timeline />);
    expect(screen.getByText(/URL: www.nztunnellers.com\/tunnellers\/26\/wwi-timeline/)).toBeInTheDocument();
  });

  test('renders url for a specific article', () => {
    render(<HowToCiteUrl id={undefined} title={'About\\Us'} timeline={false} />);
    expect(screen.getByText(/URL: www.nztunnellers.com\/history\/about-us/)).toBeInTheDocument();
  });
});

describe('HowToCiteTitle', () => {
  test('renders title for a specific tunneller', () => {
    render(<HowToCiteTitle tunneller={mockSummary} title={undefined} timeline={false} />);
    expect(screen.getByText(/John Doe[\s\S]*(1888-1975)/i)).toBeInTheDocument();
  });

  test('renders title for a specific tunneller timeline', () => {
    render(<HowToCiteTitle tunneller={mockSummary} title={undefined} timeline />);
    expect(screen.getByText(/World War I Timeline[\s\S]*of John Doe/i)).toBeInTheDocument();
  });

  test('renders title for a specific article', () => {
    render(<HowToCiteTitle tunneller={undefined} title={'About\\Us'} timeline={false} />);
    expect(screen.getByText(/About Us/)).toBeInTheDocument();
  });
});

describe('HowToCite for Profile', () => {
  const component = <HowToCite id={mockId} summary={mockSummary} today={mockToday} />;

  test('renders the component correctly', () => {
    const { asFragment } = render(component);

    expect(asFragment()).toMatchSnapshot();
  });

  describe('Name', () => {
    test('renders name correctly', () => {
      render(component);

      const element = findElementWithText('“John Doe (1888-1975)“');

      expect(element).toBeInTheDocument();
    });
  });

  describe('Dates', () => {
    test('renders birth and death dates when known', () => {
      render(component);

      const element = findElementWithText('“John Doe (1888-1975)“');

      expect(element).toBeInTheDocument();
    });

    test('renders only birth date when death date unknown', () => {
      const mockComponent = (
        <HowToCite
          id={mockId}
          summary={{ ...mockSummary, death: null }}
          today={mockToday}
        />
      );
      render(mockComponent);

      const element = findElementWithText('“John Doe (1888-†?)“');

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
});

describe('HowToCite for Article', () => {
  const component = (
    <HowToCite title={mockTitle} today={mockToday} />
  );

  test('renders the component correctly', () => {
    const { asFragment } = render(component);

    expect(asFragment()).toMatchSnapshot();
    expect(screen.getByText(/How to cite this page/)).toBeInTheDocument();
    expect(screen.getByText(/My Awesome Article Title/)).toBeInTheDocument();
    expect(screen.getByText(/4 May 2023/)).toBeInTheDocument();
    expect(screen.getByText(/www.nztunnellers.com\/history\/my-awesome-article-title./)).toBeInTheDocument();
  });
});

describe('HowToCite for Timeline', () => {
  const component = (
    <HowToCite id={mockId} summary={mockSummary} today={mockToday} timeline />
  );

  test('renders the component correctly', () => {
    const { asFragment } = render(component);

    expect(asFragment()).toMatchSnapshot();
    expect(screen.getByText(/How to cite this page/)).toBeInTheDocument();
    expect(screen.getByText(/World War I Timeline of/)).toBeInTheDocument();
    expect(screen.getByText(/John Doe/)).toBeInTheDocument();
    expect(screen.getByText(/4 May 2023/)).toBeInTheDocument();
    expect(screen.getByText(/www.nztunnellers.com\/tunnellers\/26\/wwi-timeline./)).toBeInTheDocument();
  });
});
