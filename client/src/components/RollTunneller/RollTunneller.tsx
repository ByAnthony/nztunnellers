import { Link } from 'react-router-dom';
import { Details } from '../../types/roll';
import STYLES from './RollTunneller.module.scss';

type Roll = {
    listOfTunnellers: Details[];
}

export function RollTunneller({ listOfTunnellers }: Roll) {
  return (
    <>
      {listOfTunnellers.map((tunneller: Details) => (
        <li className={STYLES.tunneller} key={tunneller.id}>
          <Link to={`/roll/${tunneller.id}`}>
            <p className={STYLES.surname}>{tunneller.name.surname}</p>
            <p className={STYLES.forename}>{tunneller.name.forename}</p>
            <p className={STYLES.serial}>{tunneller.serial}</p>
          </Link>
        </li>
      ))}
    </>
  );
}
