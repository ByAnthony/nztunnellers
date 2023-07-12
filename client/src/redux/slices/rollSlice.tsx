import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Article, Next } from '../../types/article';
import { Details } from '../../types/roll';
import { Profile } from '../../types/tunneller';

export const tunnellersApi = createApi({
  reducerPath: 'tunnellersApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getAllHistoryArticleLink: builder.query<Array<Next>, void>({
      query: () => ({
        url: 'history/',
      }),
    }),
    getHistoryArticleById: builder.query<Article, string>({
      query: (id: string) => `history/${id}`,
    }),
    getAllTunnellers: builder.query<Record<string, Array<Details>>, void>({
      query: () => ({
        url: 'tunnellers/',
      }),
    }),
    getTunnellerById: builder.query<Profile, number>({
      query: (id: number) => `tunnellers/${id}`,
    }),
  }),
});

export const {
  useGetAllHistoryArticleLinkQuery,
  useGetHistoryArticleByIdQuery,
  useGetAllTunnellersQuery,
  useGetTunnellerByIdQuery,
} = tunnellersApi;
