import '@testing-library/jest-dom/extend-expect';

import { mockMilitaryYears } from '../../../utils/mocks/mockMilitaryYears';
import { mockPostServiceYears } from '../../../utils/mocks/mockPostServiceYears';
import { render } from '../../../utils/test';

import { TimelineEvents } from './TimelineEvents';

test('should render TimelineEvents', () => {
  const { asFragment } = render(<TimelineEvents
    militaryYears={mockMilitaryYears}
    postServiceYears={mockPostServiceYears}
  />);

  expect(asFragment()).toMatchSnapshot();
});
