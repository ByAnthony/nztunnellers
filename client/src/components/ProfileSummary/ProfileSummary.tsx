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
  ) => (death ? `${birth} - ${death}` : `${birth} - †?`);

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
          <span className={STYLES.forename}>{ summary.name.forename }</span>
          <span className={STYLES.surname}>{ summary.name.surname }</span>
        </h1>
        <p className={STYLES.dates}>
          { displayBirthDeathDates(summary.birth, summary.death) }
        </p>
      </div>
      <div className={STYLES.overview}>
        <div className={STYLES['fullwidth-main-card']}>
          <p>Unit</p>
          <span>{ displayUnit(embarkationUnit.detachment, embarkationUnit.section) }</span>
        </div>
        <div className={STYLES['halfwidth-cards-container']}>
          <div className={STYLES['halfwidth-secondary-card']}>
            <div className={STYLES['halfwidth-secondary-card-title']}><p>Rank</p></div>
            <div><span>{ enlistment.rank }</span></div>
          </div>
          <div className={STYLES['halfwidth-secondary-card']}>
            <div className={STYLES['halfwidth-secondary-card-title']}><p>Serial</p></div>
            <div><span>{ enlistment.serial }</span></div>
          </div>
        </div>
      </div>
    </>
  );
}
