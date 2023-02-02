import { useState } from 'react';
import { Roll } from '../../components/Roll/Roll';
import STYLES from './RollContainer.module.scss';
import { useGetAllTunnellersQuery } from '../../redux/slices/rollSlice';

export const RollContainer = () => {

    // const [tunnellers, setAllTunnellers] = useState([]);
    const [filterByLetter, setFilterByLetter] = useState('');

    // useEffect(() => {
    //     RollService.getRollSortedByAlphabet()
    //     .then(tunnellers => setAllTunnellers(tunnellers));
    // }, []);

    // const tunnellers = useSelector((state: RootState) => state.roll);
    const tunnellers = useGetAllTunnellersQuery();
    const ListTunnellers = tunnellers.data;
    const letters = ListTunnellers === undefined ? [] : Object.keys(ListTunnellers);

    return(
        <>
            <div className={STYLES['alphabet-container']}>
                <h1>Company Roll</h1>
                <div className={STYLES['alphabet']}>
                    {letters.map(letter => <button key={letter} className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter(letter)}>{letter}</button>)}
                    <button key='All' className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter('')}>All</button>
                </div>
            </div>
            {/* <Roll filterByLetter={filterByLetter} /> */}
        </>
    );

};
