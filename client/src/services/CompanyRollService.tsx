const baseURL = "http://localhost:5000/roll/";

export const RollService = {

    getCompanyRollSortedByAlphabet(){
        return fetch(baseURL)
        .then(res => res.json());
    }

    // getTunneller(id){
    //     return fetch(baseURL + id)
    //     .then(res => res.json())
    // }

};
