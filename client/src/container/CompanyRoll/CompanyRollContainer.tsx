import {useState, useEffect} from 'react';
import {RollService} from '../../services/CompanyRollService';
import {CompanyRoll} from '../../components/CompanyRoll/CompanyRoll';

export const CompanyRollContainer = () => {

    const [roll, setAllRoll] = useState([]);

    useEffect(() => {
        RollService.getCompanyRollSortedByAlphabet()
        .then(roll => setAllRoll(roll));
    }, []);

    return(
       <CompanyRoll roll={roll} />
    );

};
