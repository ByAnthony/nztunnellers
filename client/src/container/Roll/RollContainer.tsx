import {useState, useEffect} from 'react';
import RollService from '../../services/RollService';
import {CompanyRoll} from '../../components/CompanyRoll/CompanyRoll';

const RollContainer = () => {

    const [roll, setAllRoll] = useState([]);

    useEffect(() => {
        RollService.getRollSortedByAlphabet()
        .then(roll => setAllRoll(roll))
    }, []);

    return(
       <CompanyRoll roll={roll} />
    );

};

export default RollContainer;
