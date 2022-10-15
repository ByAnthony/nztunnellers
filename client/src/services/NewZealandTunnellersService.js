const baseURL = 'http://127.0.0.1/:5000/roll/';

const NewZealandTunnellersService = {

    getRoll(){
        return fetch(baseURL)
        .then(res => res.json())
    },

    getTunneller(id){
        return fetch(baseURL + id)
        .then(res => res.json())
    }

};

export default NewZealandTunnellersService;