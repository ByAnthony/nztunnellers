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


// const initialState: InitialState = {
//   value: {},
// };

// export const rollSlice = createSlice({
//   name: UpdateRollAction,
//   initialState: initialState,
//   reducers: {
//     getRoll: (state, action: PayloadAction<Record<string, Array<Tunneller>>>) => {
//       state.value = action.payload;
//     },
//   },
// });

// export const { getRoll } = rollSlice.actions;

// export default rollSlice.reducer;
