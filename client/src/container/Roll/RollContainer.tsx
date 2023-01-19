import { useState, useEffect } from 'react';
import { RollService } from '../../services/RollService';
import { Roll } from '../../components/Roll/Roll';
import STYLES from './RollContainer.module.scss';
import { Tunneller } from '../../types';


export const RollContainer = () => {

    const [tunnellers, setAllTunnellers] = useState([]);
    const [filterByLetter, setFilterByLetter] = useState('');
    const [selectedTunneller, setSelectedTunneller] = useState<any>(null);


    useEffect(() => {
        RollService.getRollSortedByAlphabet()
        .then(tunnellers => setAllTunnellers(tunnellers));
    }, []);

    const onTunnellerSelected = (tunneller: Tunneller) => {
        setSelectedTunneller(tunneller)
    }

    const letters = Object.keys(tunnellers);

    return(
        <>
            {selectedTunneller ? console.log({selectedTunneller}) :
                (
                    <>
                        <div className={STYLES['alphabet-container']}>
                            <h1>Company Roll</h1>
                            <div className={STYLES['alphabet']}>
                                {letters.map(letter => <button key={letter} className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter(letter)}>{letter}</button>)}
                                <button key='All' className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter('')}>All</button>
                            </div>
                        </div>
                        <Roll tunnellers={tunnellers} filterByLetter={filterByLetter} onTunnellerSelected={onTunnellerSelected}/>
                    </>
                )
            }
        </>
    );

};
