import { Name } from '../../types/roll';
import STYLES from './ProfileHeader.module.scss';

type Props = {
    serial: string;
    name: Name;
    birth: string | undefined;
    death: string | undefined;
}

export function ProfileHeader({
  serial, name, birth, death,
}: Props) {
  return (
    <div className={STYLES.header}>
      <h1>
        <span className={STYLES.surname}>{ name.surname }</span>
        <span className={STYLES.forename}>{ name.forename }</span>
      </h1>
      <p className={STYLES.serial}>{ serial }</p>
      <p className={STYLES.serial}>
        Born:
        {' '}
        { birth }
      </p>
      <p className={STYLES.serial}>
        Died:
        {' '}
        { death }
      </p>
    </div>
  );
}
