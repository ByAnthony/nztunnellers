import { Death, PostWarDeath } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type props = {
  warDeath: Death | null,
  afterWarDeath: PostWarDeath | null,
}

export function DiaryDied({ warDeath, afterWarDeath }: props) {
  const title = (ageAtDeath: number | null) => (
    ageAtDeath
      ? <p>{`Died at the age of ${ageAtDeath}`}</p>
      : <p>Died</p>);

  const displayDeathInfo = (
    diedDuringWar: Death | null,
    diedAfterWar: PostWarDeath | null,
  ) => {
    if (diedDuringWar !== null && diedAfterWar === null) {
      return (
        <div className={STYLES['fullwidth-main-card']}>
          { title(diedDuringWar.ageAtDeath) }
          <span>
            { diedDuringWar.date.dayMonth !== null && diedDuringWar.date.year !== null
              ? `${diedDuringWar.date.dayMonth} ${diedDuringWar.date.year}`
              : diedDuringWar.date.year }
          </span>
        </div>
      );
    }
    if (diedDuringWar === null && diedAfterWar !== null) {
      return (
        <div className={STYLES['fullwidth-main-card']}>
          { title(diedAfterWar.ageAtDeath) }
          <span>
            { diedAfterWar.date.dayMonth !== null && diedAfterWar.date.year !== null
              ? `${diedAfterWar.date.dayMonth} ${diedAfterWar.date.year}`
              : diedAfterWar.date.year }
          </span>
        </div>
      );
    }
    return null;
  };

  return (
    <>
      { displayDeathInfo(warDeath, afterWarDeath) }
    </>
  );
}
