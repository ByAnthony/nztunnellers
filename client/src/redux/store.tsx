import { configureStore } from "@reduxjs/toolkit";
import rollReducer from "./slices/rollSlice";

export const store = configureStore({
  reducer: {
    roll: rollReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
