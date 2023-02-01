import { Tunneller } from "../../types";
import { InitialState, UpdateRollAction } from "../../types/redux/roll";
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

const initialState: InitialState = {
  value: {},
};

export const rollSlice = createSlice({
  name: UpdateRollAction,
  initialState: initialState,
  reducers: {
    getRoll: (state: any, action: PayloadAction<Record<string, Array<Tunneller>>>) => {
      state.value = action.payload;
    },
  },
});

export const { getRoll } = rollSlice.actions;

export default rollSlice.reducer;
