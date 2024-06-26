import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Article } from '../../types/article';

export const historyApi = createApi({
  reducerPath: 'historyApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getHistoryArticleById: builder.query<Article, string>({
      query: (id: string) => `history/${id}`,
    }),
  }),
});

export const {
  useGetHistoryArticleByIdQuery,
} = historyApi;
