import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Articles } from '../../types/article';

export const homepageApi = createApi({
  reducerPath: 'homepageApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getHomepageData: builder.query<Record<string, Array<Articles>>, void>({
      query: () => ({
        url: '/',
      }),
    }),
  }),
});

export const {
  useGetHomepageDataQuery,
} = homepageApi;
