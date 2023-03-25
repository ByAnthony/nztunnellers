import type { EmbarkationUnit, Enlistment, Summary } from '../../types/tunneller';
import STYLES from './ProfileSummary.module.scss';

type props = {
    summary: Summary,
    embarkationUnit: EmbarkationUnit,
    enlistment: Enlistment,
}

export function ProfileSummary({ summary, embarkationUnit, enlistment }: props) {
  const displayBirthDeathDates = (
    birth: string,
    death: string | null,
  ) => (death ? `${birth}-${death}` : `${birth}-†?`);

  const displayUnit = (
    unit: string,
    section: string | null,
  ) => {
    if (unit === 'Main Body' && section) {
      return `${unit}: ${section}`;
    }
    return unit;
  };

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
        <div className={STYLES['overview-group']}>
          <p>Unit</p>
          <p className={STYLES['overview-title']}>
            { displayUnit(embarkationUnit.detachment, embarkationUnit.section) }
          </p>
        </div>
        <div className={STYLES['overview-group']}>
          <p>Rank</p>
          <p className={STYLES['overview-title']}>{enlistment.rank}</p>
        </div>
        <div className={STYLES['overview-group']}>
          <p>Serial</p>
          <p className={STYLES['overview-title']}>{enlistment.serial}</p>
        </div>
      </div>
    </>
  );
}
