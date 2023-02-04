import { Link } from 'react-router-dom';
import { RollInfo } from '../../types/roll';
import STYLES from './RollTunneller.module.scss';

type Roll = {
    listOfTunnellers: RollInfo[];
}

export const RollTunneller = ({ listOfTunnellers }: Roll) => {
  const rollTunneller = listOfTunnellers.map((tunneller) => (
    <li className={STYLES.tunneller} key={tunneller.id}>
      <Link to={`/roll/${tunneller.id}`}>
        <p className={STYLES.surname}>{tunneller.name.surname}</p>
        <p className={STYLES.forename}>{tunneller.name.forename}</p>
        <p className={STYLES.serial}>{tunneller.serial}</p>
      </Link>
    </li>
  ));

  return (
    <>
      { rollTunneller }
      <p />
    </>
  );
};
