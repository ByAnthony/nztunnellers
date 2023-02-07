import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { Details } from '../../types/roll';
import { Profile } from '../../types/tunneller';

export const tunnellersApi = createApi({
  reducerPath: 'tunnellersApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getAllTunnellers: builder.query<Record<string, Array<Details>>, void>({
      query: () => ({
        url: 'roll/',
      }),
    }),
    getTunnellerById: builder.query<Profile, number>({
      query: (id: number) => `roll/${id}`,
    }),
  }),
});

export const { useGetAllTunnellersQuery, useGetTunnellerByIdQuery } = tunnellersApi;
