import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Homepage } from '../../types/homepage';

export const homepageApi = createApi({
  reducerPath: 'homepageApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getHomepageData: builder.query<Homepage, void>({
      query: () => ({
        url: '/',
      }),
    }),
  }),
});

export const {
  useGetHomepageDataQuery,
} = homepageApi;
