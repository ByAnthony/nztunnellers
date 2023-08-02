import { useState } from 'react';
import { RollAlphabet } from '../RollAlphabet/RollAlphabet';
import STYLES from './Roll.module.scss';
import { useGetAllTunnellersQuery } from '../../redux/slices/rollSlice';
import { Menu } from '../Menu/Menu';
import { Footer } from '../Footer/Footer';

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
          <div className={STYLES['main-title']}>
            <h1>
              <span className={STYLES['sub-title']}>The New Zealand</span>
              <span className={STYLES.title}>Tunnellers</span>
            </h1>
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
