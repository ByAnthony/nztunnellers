import '@testing-library/jest-dom/extend-expect';
import { render } from '@testing-library/react';
import { mockProfile } from '../../utils/mocks/mockProfile';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { Profile } from './Profile';

jest.mock('../../redux/slices/rollSlice', () => ({
  useGetTunnellerByIdQuery: jest.fn(),
}));

jest.mock('../../utils/date-utils', () => ({
  today: new Date('2023-05-04'),
}));

describe('Profile', () => {
  it('renders profile when data is available', () => {
    (useGetTunnellerByIdQuery as jest.Mock).mockReturnValue({
      data: mockProfile,
      error: null,
      isLoading: false,
      isSuccess: true,
    });

    const { asFragment } = render(<Profile />);

    expect(asFragment()).toMatchSnapshot();
  });

  it('does not render profile when data is undefined', () => {
    (useGetTunnellerByIdQuery as jest.Mock).mockReturnValue({
      data: undefined,
      error: null,
      isLoading: false,
      isSuccess: true,
    });

    const { container } = render(<Profile />);

    expect(container).toBeEmptyDOMElement();
  });
});
