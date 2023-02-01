import { AppDispatch } from "../store";
import { baseURL } from "./baseURL";

export const getRoll = () => {
    return (dispatch: AppDispatch) => {
      fetch(baseURL)
        .then(res => res.json())
        .then((result) => dispatch({ type: "roll", payload: result }))
    }
};
