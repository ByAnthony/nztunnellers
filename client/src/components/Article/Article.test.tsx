import '@testing-library/jest-dom/extend-expect';
import { render } from '@testing-library/react';

import { useGetHistoryArticleByIdQuery } from '../../redux/slices/rollSlice';
import { mockArticle } from '../../utils/mocks/mockArticle';

import { Article } from './Article';

jest.mock('../../redux/slices/rollSlice', () => ({
  useGetHistoryArticleByIdQuery: jest.fn(),
}));

jest.mock('../../utils/date-utils', () => ({
  today: new Date('2023-05-04'),
}));

test('renders profile when data is available', () => {
  (useGetHistoryArticleByIdQuery as jest.Mock).mockReturnValue({
    data: mockArticle,
    error: null,
    isLoading: false,
    isSuccess: true,
  });

  const { asFragment } = render(<Article />);

  expect(asFragment()).toMatchSnapshot();
});

test('does not render profile when data is undefined', () => {
  (useGetHistoryArticleByIdQuery as jest.Mock).mockReturnValue({
    data: undefined,
    error: null,
    isLoading: false,
    isSuccess: true,
  });

  const { container } = render(<Article />);

  expect(container).toBeEmptyDOMElement();
});