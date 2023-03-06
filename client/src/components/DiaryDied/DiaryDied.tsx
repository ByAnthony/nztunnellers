import { Death, PostWarDeath } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type Props = {
  birthDate: string | null,
  warDeath: Death | null,
  afterWarDeath: PostWarDeath | null,
}

export function DiaryDied({ birthDate, warDeath, afterWarDeath }: Props) {
  const title = (birth: string | null, death: string | null) => (
    death
      ? <p>{`Died at the age of ${Number(death) - Number(birth)}`}</p>
      : <p>Died</p>);

  const displayDeathInfo = (
    dateOfBirth: string | null,
    diedDuringWar: Death | null,
    diedAfterWar: PostWarDeath | null,
  ) => {
    if (diedDuringWar !== null && diedAfterWar === null) {
      return (
        <div className={STYLES['fullwidth-main-card']}>
          { title(dateOfBirth, diedDuringWar.date.year) }
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
          { title(dateOfBirth, diedAfterWar.date.year) }
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
      { displayDeathInfo(birthDate, warDeath, afterWarDeath) }
    </>
  );
}
