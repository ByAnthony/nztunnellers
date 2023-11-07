import { displayBiographyDates } from '../../../utils/displayBiographyDates';

import { Details } from '../../../types/roll';

import STYLES from './RollDetails.module.scss';

type Props = {
  listOfTunnellers: Details[];
}

export function RollDetails({ listOfTunnellers }: Props) {
  return (
    <>
      {listOfTunnellers.map((tunneller: Details) => (
        <a href={`/tunnellers/${tunneller.id}`} key={tunneller.id}>
          <div className={STYLES.tunneller}>
            <div>
              <p className={STYLES.forename}>{tunneller.name.forename}</p>
              <p className={STYLES.surname}>{tunneller.name.surname}</p>
              <p className={STYLES.dates}>
                { displayBiographyDates(tunneller.birth, tunneller.death) }
              </p>
            </div>
            <div className={STYLES.arrow}>&rarr;</div>
          </div>
        </a>
      ))}
    </>
  );
}
