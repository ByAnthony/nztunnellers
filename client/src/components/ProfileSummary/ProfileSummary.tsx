import type { Summary } from '../../types/tunneller';
import STYLES from './ProfileSummary.module.scss';

type Props = {
    summary: Summary,
}

export function ProfileSummary({ summary }: Props) {
  const displayBirthDeathDates = (birth: string | undefined, death: string | undefined) => (death ? `${birth}-${death}` : `${birth}-†?`);
  return (
    <div className={STYLES.header}>
      <h1>
        <span className={STYLES.surname}>{ summary.name.surname }</span>
        <span className={STYLES.forename}>{ summary.name.forename }</span>
      </h1>
      <p className={STYLES.dates}>
        { displayBirthDeathDates(summary.birth, summary.death) }
      </p>
    </div>
  );
}
