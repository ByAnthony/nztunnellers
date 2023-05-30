import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { DiaryWork } from './DiaryWork';
import { mockEmployment } from '../../utils/mocks/mockPreWarYears';

const component = (
  <DiaryWork employment={mockEmployment} />
);

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders employment when known', () => {
  render(component);

  expect(screen.getByText('Work')).toBeInTheDocument();
  expect(screen.getByText('Occupation')).toBeInTheDocument();
  expect(screen.getByText('Goldminer')).toBeInTheDocument();
  expect(screen.getByText('Employer')).toBeInTheDocument();
  expect(screen.getByText('Goldmining Company')).toBeInTheDocument();
});

test('renders only occupation when employer unknown', () => {
  const componentWithOccupationOnly = (
    <DiaryWork employment={{
      ...mockEmployment,
      employer: null,
    }}
    />
  );

  render(componentWithOccupationOnly);

  expect(screen.getByText('Work')).toBeInTheDocument();
  expect(screen.getByText('Occupation')).toBeInTheDocument();
  expect(screen.getByText('Goldminer')).toBeInTheDocument();
  expect(screen.queryByText('Employer')).not.toBeInTheDocument();
  expect(screen.queryByText('Goldmining Company')).not.toBeInTheDocument();
});

test('does not render employment when unknown', () => {
  const { container } = render(
    <DiaryWork employment={{
      ...mockEmployment,
      occupation: null,
      employer: null,
    }}
    />,
  );

  expect(container).toBeEmptyDOMElement();
});
