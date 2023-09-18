import { configureStore } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/dist/query';
import { tunnellersApi } from './slices/rollSlice';
import { historyApi } from './slices/historySlice';

export const store = configureStore({
  reducer: {
    [tunnellersApi.reducerPath]: tunnellersApi.reducer,
    [historyApi.reducerPath]: historyApi.reducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware()
    .concat(tunnellersApi.middleware, historyApi.middleware),
});

setupListeners(store.dispatch);

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
