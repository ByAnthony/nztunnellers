import { Name } from '../../types/roll';
import STYLES from './ProfileHeader.module.scss';

type Props = {
    serial: string | undefined;
    name: Name | undefined;
}

export function ProfileHeader({ serial, name }: Props) {
  return (
    <div className={STYLES.header}>
      <h1>
        <span className={STYLES.surname}>{ name?.surname }</span>
        <span className={STYLES.forename}>{ name?.forename }</span>
      </h1>
      <p className={STYLES.serial}>{ serial }</p>
    </div>
  );
}
