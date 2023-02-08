import { Link } from 'react-router-dom';
import { Details } from '../../types/roll';
import STYLES from './RollDetails.module.scss';

type Roll = {
    listOfTunnellers: Details[];
}

export function RollDetails({ listOfTunnellers }: Roll) {
  return (
    <>
      {listOfTunnellers.map((tunneller: Details) => (
        <Link to={`/roll/${tunneller.id}`} key={tunneller.id}>
          <div className={STYLES.tunneller}>
            <p className={STYLES.surname}>{tunneller.name.surname}</p>
            <p className={STYLES.forename}>{tunneller.name.forename}</p>
            <p className={STYLES.serial}>{tunneller.serial}</p>
          </div>
        </Link>
      ))}
    </>
  );
}
