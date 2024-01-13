import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Article, Articles } from '../../types/article';

export const historyApi = createApi({
  reducerPath: 'historyApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getAllHistoryArticleLink: builder.query<Array<Articles>, void>({
      query: () => ({
        url: '/',
      }),
    }),
    getHistoryArticleById: builder.query<Article, string>({
      query: (id: string) => `history/${id}`,
    }),
  }),
});

export const {
  useGetAllHistoryArticleLinkQuery,
  useGetHistoryArticleByIdQuery,
} = historyApi;
