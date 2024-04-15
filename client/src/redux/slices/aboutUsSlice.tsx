import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Article } from '../../types/article';

export const aboutUsApi = createApi({
  reducerPath: 'aboutUsApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getAboutUs: builder.query<Article, void>({
      query: () => ({
        url: '/about-us',
      }),
    }),
  }),
});

export const {
  useGetAboutUsQuery,
} = aboutUsApi;
