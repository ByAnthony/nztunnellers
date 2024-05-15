import { configureStore } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/dist/query';
import { tunnellersApi } from './slices/rollSlice';
import { historyApi } from './slices/historySlice';
import { aboutUsApi } from './slices/aboutUsSlice';
import { homepageApi } from './slices/homepageSlice';

export const store = configureStore({
  reducer: {
    [homepageApi.reducerPath]: homepageApi.reducer,
    [tunnellersApi.reducerPath]: tunnellersApi.reducer,
    [historyApi.reducerPath]: historyApi.reducer,
    [aboutUsApi.reducerPath]: aboutUsApi.reducer,
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware()
    .concat(
      homepageApi.middleware,
      tunnellersApi.middleware,
      historyApi.middleware,
      aboutUsApi.middleware,
    ),
});

setupListeners(store.dispatch);

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
