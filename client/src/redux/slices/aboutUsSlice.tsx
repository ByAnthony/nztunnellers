import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { AboutUs } from '../../types/about-us';

export const aboutUsApi = createApi({
  reducerPath: 'aboutUsApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getAboutUs: builder.query<AboutUs, void>({
      query: () => ({
        url: '/about-us',
      }),
    }),
  }),
});

export const {
  useGetAboutUsQuery,
} = aboutUsApi;
