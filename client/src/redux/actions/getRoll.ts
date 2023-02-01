import { baseURL } from "./baseURL";

export const getRoll = () => {
    return fetch(baseURL)
      .then(res => res.json())
};
