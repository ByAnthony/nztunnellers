import type { EmbarkationUnit, Enlistment, Summary } from '../../types/tunneller';
import STYLES from './ProfileSummary.module.scss';

type Props = {
    summary: Summary,
    embarkationUnit: EmbarkationUnit,
    enlistment: Enlistment,
}

export function ProfileSummary({ summary, embarkationUnit, enlistment }: Props) {
  const displayBirthDeathDates = (birth: string | undefined, death: string | undefined) => (death ? `${birth}-${death}` : `${birth}-†?`);
  return (
    <>
      <div className={STYLES.header}>
        <h1>
          <span className={STYLES.surname}>{ summary.name.surname }</span>
          <span className={STYLES.forename}>{ summary.name.forename }</span>
        </h1>
        <p className={STYLES.dates}>
          { displayBirthDeathDates(summary.birth, summary.death) }
        </p>
      </div>
      <div className={STYLES.overview}>
        <div className={STYLES.unit}>
          <h3>Unit</h3>
          <p>{embarkationUnit.detachment}</p>
        </div>
        <div className={STYLES.unit}>
          <h3>Rank</h3>
          <p>{enlistment.rank}</p>
        </div>
        <div className={STYLES.unit}>
          <h3>Serial</h3>
          <p>{enlistment.serial}</p>
        </div>
      </div>
    </>
  );
}
