import { ReactNode } from 'react';
import { renderHook, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import fetchMock from 'jest-fetch-mock';
import { mockRoll } from '../../utils/mocks/mockRoll';
import { mockProfile } from '../../utils/mocks/mockProfile';
import { store } from '../store';
import { useGetAllTunnellersQuery, useGetTunnellerByIdQuery } from './rollSlice';

function Wrapper({ children }: { children: ReactNode }) {
  return (
    <Provider store={store}>
      {children}
    </Provider>
  );
}

describe('useGetAllTunnellersQuery', () => {
  const endpointName = 'getAllTunnellers';
  const data = mockRoll;

  beforeEach(() => {
    fetchMock.resetMocks();
    fetchMock.mockOnceIf('http://localhost:5000/tunnellers/', () => Promise.resolve({
      status: 200,
      body: JSON.stringify({ data }),
    }));
  });

  it('renders hook', async () => {
    const { result } = renderHook(() => useGetAllTunnellersQuery(), {
      wrapper: Wrapper,
    });

    expect(result.current).toMatchObject({
      status: 'pending',
      endpointName,
      isLoading: true,
      isSuccess: false,
      isError: false,
      isFetching: true,
    });

    await waitFor(() => expect(result.current.isSuccess).toBe(true));
    expect(fetchMock).toBeCalledTimes(1);

    expect(result.current).toMatchObject({
      status: 'fulfilled',
      endpointName,
      data: { data },
      isLoading: false,
      isSuccess: true,
      isError: false,
      currentData: {},
      isFetching: false,
    });
  });
});

describe('useGetTunnellerByIdQuery', () => {
  const endpointName = 'getTunnellerById';
  const tunneller = 1;
  const data = mockProfile;

  beforeEach(() => {
    fetchMock.resetMocks();
    fetchMock.mockOnceIf(`http://localhost:5000/tunnellers/${tunneller}`, () => Promise.resolve({
      status: 200,
      body: JSON.stringify({ data }),
    }));
  });

  it('renders hook', async () => {
    const { result } = renderHook(() => useGetTunnellerByIdQuery(tunneller), {
      wrapper: Wrapper,
    });

    expect(result.current).toMatchObject({
      status: 'pending',
      endpointName,
      isLoading: true,
      isSuccess: false,
      isError: false,
      isFetching: true,
    });

    await waitFor(() => expect(result.current.isSuccess).toBe(true));
    expect(fetchMock).toBeCalledTimes(1);

    expect(result.current).toMatchObject({
      status: 'fulfilled',
      endpointName,
      data: { data },
      isLoading: false,
      isSuccess: true,
      isError: false,
      currentData: {},
      isFetching: false,
    });
  });
});
