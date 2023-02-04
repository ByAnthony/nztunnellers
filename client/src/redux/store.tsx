import { configureStore } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/dist/query';
import { tunnellersApi } from './slices/rollSlice';

export const store = configureStore({
  reducer: {
    [tunnellersApi.reducerPath]: tunnellersApi.reducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(tunnellersApi.middleware),
});

setupListeners(store.dispatch);

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
