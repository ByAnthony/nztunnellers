import { Link } from 'react-router-dom';
import { Details } from '../../types/roll';
import STYLES from './RollDetails.module.scss';
import { displayBirthDeathDates } from '../../utils/utils';

type Roll = {
    listOfTunnellers: Details[];
}

export function RollDetails({ listOfTunnellers }: Roll) {
  return (
    <>
      {listOfTunnellers.map((tunneller: Details) => (
        <Link to={`/tunnellers/${tunneller.id}`} key={tunneller.id} className={STYLES['tunneller-link']}>
          <div className={STYLES.tunneller}>
            <div>
              <p className={STYLES.forename}>{tunneller.name.forename}</p>
              <p className={STYLES.surname}>{tunneller.name.surname}</p>
              <p className={STYLES.dates}>
                { displayBirthDeathDates(tunneller.birth, tunneller.death) }
              </p>
            </div>
            <div className={STYLES['arrow-right']}>&rarr;</div>
          </div>
        </Link>
      ))}
    </>
  );
}
