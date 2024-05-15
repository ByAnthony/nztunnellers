import { ReactNode } from 'react';
import { renderHook, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import fetchMock from 'jest-fetch-mock';
import { store } from '../store';
import { useGetHomepageDataQuery } from './homepageSlice';

function Wrapper({ children }: { children: ReactNode }) {
  return (
    <Provider store={store}>
      {children}
    </Provider>
  );
}

describe('useGetAllHistoryArticleLinkQuery', () => {
  const endpointName = 'getHomepageData';
  const data = {
    tunnellers: [
      { id: 1, image: 'image-1.jpg' },
      { id: 2, image: 'image-2.jpg' },
      { id: 3, image: 'image-3.jpg' },
    ],
    historyChapters: [
      { url: 'test-article-1', title: 'test-article-1', chapter: 1 },
      { url: 'test-article-2', title: 'test-article-2', chapter: 2 },
      { url: 'test-article-3', title: 'test-article-3', chapter: 3 },
    ],
  };

  beforeEach(() => {
    fetchMock.resetMocks();
    fetchMock.mockOnceIf('http://localhost:5000/', () => Promise.resolve({
      status: 200,
      body: JSON.stringify({ data }),
    }));
  });

  it('renders hook', async () => {
    const { result } = renderHook(() => useGetHomepageDataQuery(), {
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
