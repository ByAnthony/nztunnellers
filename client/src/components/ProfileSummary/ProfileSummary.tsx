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
          <span>{ summary.name.forename }</span>
          <span className={STYLES.surname}>{ summary.name.surname }</span>
        </h1>
        <p className={STYLES.dates}>
          { displayBirthDeathDates(summary.birth, summary.death) }
        </p>
      </div>
      <div className={STYLES.overview}>
        <table>
          <tbody>
            <tr>
              <th>Unit</th>
              <th>Serial</th>
              <th>Rank</th>
            </tr>
            <tr>
              <td>{ displayUnit(embarkationUnit.detachment, embarkationUnit.section) }</td>
              <td>{enlistment.serial}</td>
              <td>{enlistment.rank}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </>
  );
}
