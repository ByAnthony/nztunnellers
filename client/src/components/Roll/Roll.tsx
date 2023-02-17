import { useState } from 'react';
import { RollAlphabet } from '../RollAlphabet/RollAlphabet';
import STYLES from './Roll.module.scss';
import { useGetAllTunnellersQuery } from '../../redux/slices/rollSlice';

export function Roll() {
  const [filterByLetter, setFilterByLetter] = useState('');

  const {
    data, error, isLoading, isSuccess,
  } = useGetAllTunnellersQuery();

  if (data) {
    const letters = Object.keys(data);
    return (
      <>
        {error && (
          <div className={STYLES['alphabet-container']}>
            <p>An error occured</p>
          </div>
        )}
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
          <RollAlphabet tunnellers={data} filterByLetter={filterByLetter} />
        </>
        )}
      </>
    );
  }
  return null;
}
