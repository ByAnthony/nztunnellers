import '@testing-library/jest-dom';
import { render } from '@testing-library/react';
import { Provider } from 'react-redux';
import { store } from '../../redux/store';
import { mockId, mockProfile } from '../../utils/mocks/mockProfile';
import { Profile } from './Profile';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';

jest.mock('../../redux/slices/rollSlice');

jest.mock('react-router-dom', () => ({
  useParams: jest.fn(),
}));

jest.spyOn(global, 'Number');

beforeAll(() => {
  (useGetTunnellerByIdQuery as jest.MockedFunction<typeof useGetTunnellerByIdQuery>)
    .mockReturnValue({ data: mockProfile, refetch: jest.fn() });
});

describe('YourComponent', () => {
  it('should mock the code snippet', () => {
    jest.requireMock('react-router-dom').useParams.mockReturnValue({ id: mockId });

    const { asFragment } = render(
      <Provider store={store}>
        <Profile />
      </Provider>,
    );

    expect(jest.requireMock('react-router-dom').useParams).toHaveBeenCalled();
    expect(global.Number).toHaveBeenCalledWith(mockId);
    expect(asFragment()).toMatchSnapshot();
  });
});
