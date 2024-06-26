import { ReactNode } from 'react';
import { renderHook, waitFor } from '@testing-library/react';
import { Provider } from 'react-redux';
import fetchMock from 'jest-fetch-mock';
import { mockArticle } from '../../utils/mocks/mockArticle';
import { store } from '../store';
import { useGetHistoryArticleByIdQuery } from './historySlice';

function Wrapper({ children }: { children: ReactNode }) {
  return (
    <Provider store={store}>
      {children}
    </Provider>
  );
}

describe('useGetHistoryArticleByIdQuery', () => {
  const endpointName = 'getHistoryArticleById';
  const article = 'test-article';
  const data = mockArticle;

  beforeEach(() => {
    fetchMock.resetMocks();
    fetchMock.mockOnceIf(`http://localhost:5000/history/${article}`, () => Promise.resolve({
      status: 200,
      body: JSON.stringify({ data }),
    }));
  });

  it('renders hook', async () => {
    const { result } = renderHook(() => useGetHistoryArticleByIdQuery(article), {
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
