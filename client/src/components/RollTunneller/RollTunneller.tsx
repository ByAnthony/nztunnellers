import { Link } from 'react-router-dom';
import { RollInfo } from '../../types/roll';
import STYLES from './RollTunneller.module.scss';

type Roll = {
    listOfTunnellers: RollInfo[];
}

export function RollTunneller({ listOfTunnellers }: Roll) {
  return (
    <>
      {listOfTunnellers.map((tunneller) => (
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
