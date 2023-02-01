import { useState } from 'react';
import { Roll } from '../../components/Roll/Roll';
import STYLES from './RollContainer.module.scss';
import { useSelector } from 'react-redux';

export const RollContainer = () => {

    // const [tunnellers, setAllTunnellers] = useState([]);
    const [filterByLetter, setFilterByLetter] = useState('');

    // useEffect(() => {
    //     RollService.getRollSortedByAlphabet()
    //     .then(tunnellers => setAllTunnellers(tunnellers));
    // }, []);

    const tunnellers = useSelector((state: any) => state.roll.value)
    const letters = Object.keys(tunnellers);

    return(
        <>
            <div className={STYLES['alphabet-container']}>
                <h1>Company Roll</h1>
                <div className={STYLES['alphabet']}>
                    {letters.map(letter => <button key={letter} className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter(letter)}>{letter}</button>)}
                    <button key='All' className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter('')}>All</button>
                </div>
            </div>
            <Roll tunnellers={tunnellers} filterByLetter={filterByLetter} />
        </>
    );

};
