import { render } from '@testing-library/react';

import { mockProfile } from '../../utils/mocks/mockProfile';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { Timeline } from './Timeline';

jest.mock('../../redux/slices/rollSlice', () => ({
  useGetTunnellerByIdQuery: jest.fn(),
}));

jest.mock('../../utils/date', () => ({
  today: new Date('2023-05-04'),
}));

test('renders profile when data is available', () => {
  (useGetTunnellerByIdQuery as jest.Mock).mockReturnValue({
    data: mockProfile,
    error: null,
    isLoading: false,
    isSuccess: true,
  });

  const { asFragment } = render(<Timeline />);

  expect(asFragment()).toMatchSnapshot();
});
