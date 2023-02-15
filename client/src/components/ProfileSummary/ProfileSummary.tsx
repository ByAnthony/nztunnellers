import type { Summary } from '../../types/tunneller';
import STYLES from './ProfileSummary.module.scss';

type Props = {
    summary: Summary,
}

export function ProfileSummary({ summary }: Props) {
  return (
    <div className={STYLES.header}>
      <h1>
        <span className={STYLES.surname}>{ summary.name.surname }</span>
        <span className={STYLES.forename}>{ summary.name.forename }</span>
      </h1>
      {/* <p className={STYLES.serial}>{ summary.serial }</p> */}
      <p className={STYLES.dates}>
        { summary.birth.year }
        {' - '}
        { summary.death.year }
      </p>
    </div>
  );
}
