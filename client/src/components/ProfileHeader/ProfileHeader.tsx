import { Name } from '../../types/roll';
import STYLES from './ProfileHeader.module.scss';

type Props = {
    serial: string | undefined;
    name: Name | undefined;
}

export function ProfileHeader({ serial, name }: Props) {
  return (
    <div className={STYLES.header}>
      <p className={STYLES.surname}>{ name?.surname }</p>
      <p className={STYLES.forename}>{ name?.forename }</p>
      <p className={STYLES.serial}>{ serial }</p>
    </div>
  );
}
