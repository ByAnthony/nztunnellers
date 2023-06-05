import '@testing-library/jest-dom';
import { render } from '@testing-library/react';
import { mockMedals } from '../../utils/mocks/mockMilitaryYears';
import { DiaryMedal } from './DiaryMedal';

const component = (<DiaryMedal medals={mockMedals} />);

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});
