import { configureStore } from "@reduxjs/toolkit";
import { tunnellersApi } from "./slices/rollSlice";
import { setupListeners } from "@reduxjs/toolkit/dist/query";

export const store = configureStore({
  reducer: {
    [tunnellersApi.reducerPath]: tunnellersApi.reducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(tunnellersApi.middleware),
});

setupListeners(store.dispatch)

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
