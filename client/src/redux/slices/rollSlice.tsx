import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";
import { RollInfo } from "../../types/roll";
import { Tunneller } from "../../types/tunneller";

export const tunnellersApi = createApi({
  reducerPath: 'tunnellersApi',
  baseQuery: fetchBaseQuery({
    baseUrl: 'http://localhost:5000/',
  }),
  endpoints: (builder) => ({
    getAllTunnellers: builder.query<Record<string, Array<RollInfo>>, void>({
      query: () => ({
        url: 'roll/',
      }),
    }),
    getTunnellerById: builder.query<Tunneller, number>({
      query: (id: number) => `roll/${id}`,
      })
    })
  });

export const { useGetAllTunnellersQuery, useGetTunnellerByIdQuery } = tunnellersApi;
