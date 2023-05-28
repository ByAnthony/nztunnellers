import { Birth, Date } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type props = {
    birth: Birth,
}

export function DiaryBirth({ birth }: props) {
  const displayBirthInfo = (birthCountry: string | null, birthDate: Date | null) => {
    if (birthDate !== null && birthCountry !== null) {
      return (
        <div className={STYLES['fullwidth-main-card']}>
          <p>
            {`Born in ${birthCountry}`}
          </p>
          <span>{ `${birthDate?.dayMonth} ${birthDate?.year}` }</span>
        </div>
      );
    }
    if (birthDate !== null && birthCountry === null) {
      return (
        <div className={STYLES['fullwidth-main-card']}>
          <p>Born</p>
          <span>{ `${birthDate?.dayMonth} ${birthDate?.year}` }</span>
        </div>
      );
    }
    if (birthDate === null && birthCountry !== null) {
      return (
        <div className={STYLES['fullwidth-main-card']}>
          <span>{ `Born in ${birthCountry}` }</span>
        </div>
      );
    }
    return null;
  };

  return (
    <>
      { displayBirthInfo(birth.country, birth.date) }
    </>
  );
}
