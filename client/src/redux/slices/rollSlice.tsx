import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { Tunneller } from "../../types";

export const tunnellersApi = createApi({
  reducerPath: 'tunnellersApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getAllTunnellers: builder.query<Record<string, Array<Tunneller>>, void>({
      query: () => ({
        url: 'roll/',
      }),
    }),
    getTunnellersById: builder.query<Tunneller, void>({
      query: (id) => ({
        url: `roll/${id}`,
      })
    })
  })
});

export const { useGetAllTunnellersQuery, useGetTunnellersByIdQuery } = tunnellersApi;
