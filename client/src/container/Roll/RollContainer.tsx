import {useState, useEffect} from 'react';
import RollService from '../../services/RollService';
import {Roll} from '../../components/Roll/Roll';

const RollContainer = () => {

    const [tunnellers, setAllTunnellers] = useState([]);

    useEffect(() => {
        RollService.getRoll()
        .then(tunnellers => setAllTunnellers(tunnellers))
    }, []);

    return(
       <Roll tunnellers={tunnellers} />
    );

}

export default RollContainer;
