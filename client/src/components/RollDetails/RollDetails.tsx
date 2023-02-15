import { Link } from 'react-router-dom';
import { Details } from '../../types/roll';
import STYLES from './RollDetails.module.scss';

type Roll = {
    listOfTunnellers: Details[];
}

export function RollDetails({ listOfTunnellers }: Roll) {
  const displayBirthDeathDates = (birth: string | undefined, death: string | undefined) => (death ? `${birth}-${death}` : `${birth}-†?`);
  return (
    <>
      {listOfTunnellers.map((tunneller: Details) => (
        <Link to={`/roll/${tunneller.id}`} key={tunneller.id}>
          <div className={STYLES.tunneller}>
            <p className={STYLES.surname}>{tunneller.name.surname}</p>
            <p className={STYLES.forename}>{tunneller.name.forename}</p>
            <p className={STYLES.dates}>
              { displayBirthDeathDates(tunneller.birth, tunneller.death) }
            </p>
          </div>
        </Link>
      ))}
    </>
  );
}
