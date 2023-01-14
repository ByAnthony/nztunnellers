import { useState, useEffect } from 'react';
import { RollService } from '../../services/RollService';
import { Roll } from '../../components/Roll/Roll';
import STYLES from './RollContainer.module.scss';


export const RollContainer = () => {

    const [tunnellers, setAllTunnellers] = useState([]);
    const [filterByLetter, setFilterByLetter] = useState('');


    useEffect(() => {
        RollService.getRollSortedByAlphabet()
        .then(tunnellers => setAllTunnellers(tunnellers));
    }, []);

    const letters = Object.keys(tunnellers);

    return(
        <>
            <div className={STYLES['alphabet-container']}>
                <div className={STYLES['alphabet']}>
                    {letters.map(letter => <button key={letter} className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter(letter)}>{letter}</button>)}
                    <button key='All' className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter('')}>All</button>
                </div>
            </div>
            <Roll tunnellers={tunnellers} filterByLetter={filterByLetter}/>
        </>
    );

};
