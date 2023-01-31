const baseURL = "http://localhost:5000/roll/";

export const RollService = {

    getRollSortedByAlphabet(){
        return fetch(baseURL)
        .then(res => res.json());
    },

    getTunneller(id: number){
        return fetch(baseURL + id)
        .then(res => res.json())
    }
};
