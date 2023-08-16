import { useState } from 'react';
import { useGetAllTunnellersQuery } from '../../redux/slices/rollSlice';

import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';
import { RollAlphabet } from '../RollAlphabet/RollAlphabet';

import STYLES from './Roll.module.scss';

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
          <div className={STYLES.container}>
            <p>An error occured</p>
          </div>
        )}
        <Menu />
        { isLoading }
        { isSuccess && (
        <div className={STYLES.container}>
          <div className={STYLES.header}>
            <div className={STYLES['main-title']}>
              <h1>
                <span className={STYLES['title-line-1']}>The New Zealand</span>
                <span className={STYLES['title-line-2']}>Tunnellers</span>
              </h1>
            </div>
          </div>
          <div className={STYLES['roll-container']}>
            <div className={STYLES.alphabet}>
              {letters.map((letter) => <button type="button" key={letter} className={STYLES.letter} onClick={() => setFilterByLetter(letter)} aria-label={`Filter names by the letter ${letter}`}>{letter}</button>)}
              <button type="button" key="All" className={STYLES.letter} onClick={() => setFilterByLetter('')} aria-label="Remove the filter by name">All</button>
            </div>
            <RollAlphabet tunnellers={data} filterByLetter={filterByLetter} />
          </div>
        </div>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
