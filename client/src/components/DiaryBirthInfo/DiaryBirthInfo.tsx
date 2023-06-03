import { Birth } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type props = {
    birth: Birth,
}

export function DiaryBirth({ birth }: props) {
  if (birth.date !== null && birth.country !== null) {
    return (
      <div className={STYLES['fullwidth-main-card']}>
        <p>
          {`Born in ${birth.country}`}
        </p>
        <span>{ `${birth.date?.dayMonth} ${birth.date?.year}` }</span>
      </div>
    );
  }
  if (birth.date !== null && birth.country === null) {
    return (
      <div className={STYLES['fullwidth-main-card']}>
        <p>Born</p>
        <span>{ `${birth.date?.dayMonth} ${birth.date?.year}` }</span>
      </div>
    );
  }
  if (birth.date === null && birth.country !== null) {
    return (
      <div className={STYLES['fullwidth-main-card']}>
        <span>{ `Born in ${birth.country}` }</span>
      </div>
    );
  }
  return null;
}
