import { Death, PostWarDeath } from '../../../../types/tunneller';

import STYLES from '../ProfileDiary.module.scss';

type Props = {
  warDeath: Death | null;
  afterWarDeath: PostWarDeath | null;
}

export function DiaryDied({ warDeath, afterWarDeath }: Props) {
  const title = (ageAtDeath: number | null) => (
    ageAtDeath
      ? <p>{`Died at the age of ${ageAtDeath}`}</p>
      : <p>Died</p>);
  if (warDeath !== null && afterWarDeath === null) {
    return (
      <>
        <h2>Death</h2>
        <div className={STYLES['fullwidth-main-card']}>
          { title(warDeath.ageAtDeath) }
          <span>
            { warDeath.date.dayMonth !== null && warDeath.date.year !== null
              ? `${warDeath.date.dayMonth} ${warDeath.date.year}`
              : warDeath.date.year }
          </span>
        </div>
      </>
    );
  }
  if (warDeath === null && afterWarDeath !== null) {
    return (
      <>
        <h2>Death</h2>
        <div className={STYLES['fullwidth-main-card']}>
          { title(afterWarDeath.ageAtDeath) }
          <span>
            { afterWarDeath.date.dayMonth !== null && afterWarDeath.date.year !== null
              ? `${afterWarDeath.date.dayMonth} ${afterWarDeath.date.year}`
              : afterWarDeath.date.year }
          </span>
        </div>
      </>
    );
  }
  return null;
}
