import { Birth, Date } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type Props = {
    birth: Birth,
}

export function DiaryBirth({ birth }: Props) {
  const displayBirthCountry = (country: string | null) => (
    country !== null ? (
      <p>
        {`Born in ${country}`}
      </p>
    ) : <p>Born</p>
  );

  const displayBirthDate = (birthDate: Date) => (
    birthDate.dayMonth !== null ? (
      <span>{ `${birthDate.dayMonth} ${birthDate.year}` }</span>
    ) : <span>{ `${birthDate.year}` }</span>
  );

  const displayBirthInfo = (birthCountry: string | null, birthDate: Date) => (
    <div className={STYLES['fullwidth-secondary-card']}>
      { displayBirthCountry(birthCountry) }
      { displayBirthDate(birthDate) }
    </div>
  );

  return (
    <>
      { displayBirthInfo(birth.country, birth.date) }
    </>
  );
}
