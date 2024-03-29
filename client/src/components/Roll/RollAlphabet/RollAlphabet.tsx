import { Details } from '../../../types/roll';
import { RollDetails } from '../RollDetails/RollDetails';

import STYLES from './RollAlphabet.module.scss';

type Props = {
    tunnellers: Record<string, Details[]>;
    filterByLetter: string;
};

export function RollAlphabet({ tunnellers, filterByLetter }: Props) {
  const tunnellersList = Object.entries(tunnellers);

  const isFilteredByLetter = (letter: string) => (letter === '' ? tunnellersList : tunnellersList.filter((key) => key.includes(letter)));

  return (
    <div className={STYLES.roll}>
      {isFilteredByLetter(filterByLetter)
        .map(([key, listOfTunnellers]) => (
          <div id={`letter-${key}`} key={key}>
            <div className={STYLES['letter-container']}>
              <h2 className={STYLES.title} key={key} aria-label={`Letter ${key}`}>{key}</h2>
            </div>
            <div className={STYLES['tunnellers-container']}>
              <RollDetails listOfTunnellers={listOfTunnellers} />
            </div>
          </div>
        ))}
    </div>
  );
}
