import { render } from '@testing-library/react';
import { mockProfile } from '../../utils/mocks/mockProfile';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { Profile } from './Profile';

jest.mock('../../redux/slices/rollSlice', () => ({
  useGetTunnellerByIdQuery: jest.fn(),
}));

describe('Profile', () => {
  it('renders profile information when data is available', () => {
    (useGetTunnellerByIdQuery as jest.Mock).mockReturnValue({
      data: mockProfile,
      error: null,
      isLoading: false,
      isSuccess: true,
    });

    const { asFragment } = render(<Profile />);

    expect(asFragment()).toMatchSnapshot();
  });

  // it('does not render profile information when data is unavailable', () => {
  //   (useGetTunnellerByIdQuery as jest.Mock).mockReturnValue({
  //     data: undefined,
  //     error: null,
  //     isLoading: false,
  //     isSuccess: true,
  //   });

  //   const { container } = render(<Profile />);

  //   expect(container).toBeEmptyDOMElement();
  // });
});
