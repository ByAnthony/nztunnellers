const baseURL = "http://localhost:5000/roll/";

const RollService = {

    getRoll(){
        return fetch(baseURL)
        .then(res => res.json())
    }

    // getTunneller(id){
    //     return fetch(baseURL + id)
    //     .then(res => res.json())
    // }

};

export default RollService;
