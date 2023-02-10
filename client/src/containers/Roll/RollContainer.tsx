import { useState } from 'react';
import { Roll } from '../../components/Roll/Roll';
import STYLES from './RollContainer.module.scss';
import { useGetAllTunnellersQuery } from '../../redux/slices/rollSlice';

export function RollContainer() {
  const [filterByLetter, setFilterByLetter] = useState('');

  const { data, isLoading, isSuccess } = useGetAllTunnellersQuery();

  if (data) {
    const letters = Object.keys(data);
    return (
      <>
        { isLoading }
        { isSuccess && (
        <>
          <div className={STYLES['alphabet-container']}>
            <h1>Company Roll</h1>
            <div className={STYLES.alphabet}>
              {letters.map((letter) => <button type="button" key={letter} className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter(letter)}>{letter}</button>)}
              <button type="button" key="All" className={STYLES['alphabet-letter']} onClick={() => setFilterByLetter('')}>All</button>
            </div>
          </div>
          <Roll tunnellers={data} filterByLetter={filterByLetter} />
        </>
        )}
      </>
    );
  }
  return null;
}
