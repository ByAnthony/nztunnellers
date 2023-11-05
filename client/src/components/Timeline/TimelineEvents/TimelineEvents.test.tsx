import '@testing-library/jest-dom/extend-expect';
import { screen } from '@testing-library/react';

import { mockMilitaryYears } from '../../../utils/mocks/mockMilitaryYears';
import { mockPostServiceYears } from '../../../utils/mocks/mockPostServiceYears';
import { render } from '../../../utils/test';

import { TimelineEvents } from './TimelineEvents';

test('should render a timeline', () => {
  render(<TimelineEvents
    militaryYears={mockMilitaryYears}
    postServiceYears={mockPostServiceYears}
  />);

  expect(screen.getByText('Enlisted')).toBeInTheDocument();
  expect(screen.getByText('Main Body')).toBeInTheDocument();
});
