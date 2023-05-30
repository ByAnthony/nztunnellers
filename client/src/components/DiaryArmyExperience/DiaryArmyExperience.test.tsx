import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { mockId } from '../../utils/mocks/mockProfile';
import { mockArmyExperience, mockArmyExperienceList } from '../../utils/mocks/mockPreWarYears';
import { DiaryArmyExperience } from './DiaryArmyExperience';

const component = (
  <DiaryArmyExperience tunnellerId={mockId} armyExperience={mockArmyExperienceList} />
);

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders army experience when known', () => {
  render(component);

  expect(screen.getByText('NZ Infantry')).toBeInTheDocument();
  expect(screen.getByText('12 months in New Zealand')).toBeInTheDocument();
});

test('renders army experience when duration unknown', () => {
  const componentWithoutDuration = (
    <DiaryArmyExperience
      tunnellerId={mockId}
      armyExperience={[
        {
          ...mockArmyExperience,
          duration: null,
        },
      ]}
    />
  );

  render(componentWithoutDuration);

  expect(screen.getByText('NZ Infantry')).toBeInTheDocument();
  expect(screen.getByText('New Zealand')).toBeInTheDocument();
});

test('renders army experience when country unknown', () => {
  const componentWithoutDuration = (
    <DiaryArmyExperience
      tunnellerId={mockId}
      armyExperience={[
        {
          ...mockArmyExperience,
          country: null,
        },
      ]}
    />
  );

  render(componentWithoutDuration);

  expect(screen.getByText('NZ Infantry')).toBeInTheDocument();
  expect(screen.getByText('12 months')).toBeInTheDocument();
});

test('renders army experience when country and duration unknown', () => {
  const componentWithoutDuration = (
    <DiaryArmyExperience
      tunnellerId={mockId}
      armyExperience={[
        {
          ...mockArmyExperience,
          country: null,
          duration: null,
        },
      ]}
    />
  );

  render(componentWithoutDuration);

  expect(screen.getByText('NZ Infantry')).toBeInTheDocument();
  expect(screen.queryByText('12 months')).not.toBeInTheDocument();
  expect(screen.queryByText('New Zealand')).not.toBeInTheDocument();
});

// test('renders conflict experience', () => {
//   const componentWithoutDuration = (
//     <DiaryArmyExperience
//       tunnellerId={mockId}
//       armyExperience={[mockArmyExperience({
//         unit: 'Other',
//         country: null,
//         conflict: 'South Africa War',
//         duration: '2 years',
//       })]}
//     />
//   );

//   render(componentWithoutDuration);

//   expect(screen.getByText('NZ Infantry')).toBeInTheDocument();
//   expect(screen.queryByText('12 months')).not.toBeInTheDocument();
//   expect(screen.queryByText('New Zealand')).not.toBeInTheDocument();
// });

test('does not render army experience when unknown', () => {
  render(
    <DiaryArmyExperience tunnellerId={mockId} armyExperience={[]} />,
  );

  expect(screen.queryByText('NZ Infantry')).not.toBeInTheDocument();
  expect(screen.queryByText('12 months in New Zealand')).not.toBeInTheDocument();
});
