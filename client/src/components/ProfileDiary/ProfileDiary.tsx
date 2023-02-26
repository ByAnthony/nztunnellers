import {
  Date, Origins, Parent, Parents,
} from '../../types/tunneller';
import STYLES from './ProfileDiary.module.scss';

type Props = {
  origins: Origins;
}

export function ProfileDiary({ origins }: Props) {
  const displayBirthCountry = (country: string | undefined) => (
    country !== null ? (
      <p>
        Born in
        {' '}
        {country}
      </p>
    ) : <p>Born</p>
  );

  const displayBirthDate = (birth: Date) => (
    birth.dayMonth !== null ? (
      `${birth.dayMonth} ${birth.year}`
    ) : `${birth.year}`
  );

  const displayParents = (parents: Parents) => {
    if (parents.mother !== null || parents.father !== null) {
      const nonNullishParent = (
        parent: Parent | undefined,
      ) => (parent !== null ? parent?.name : 'Unknown');

      return (
        <div className={STYLES['card-container']}>
          <div className={STYLES['secondary-card']}>
            <div className={STYLES['secondary-card-title']}><p>Mother</p></div>
            <div>{ nonNullishParent(origins.parents.mother) }</div>
          </div>
          <div className={STYLES['secondary-card']}>
            <div className={STYLES['secondary-card-title']}><p>Father</p></div>
            <div>{ nonNullishParent(origins.parents.father) }</div>
          </div>
        </div>
      );
    }
    return null;
  };

  return (
    <div className={STYLES.diary}>
      <h2>Diary</h2>
      <div className={STYLES['main-card']}>
        { displayBirthCountry(origins.birth.country) }
        { displayBirthDate(origins.birth.date) }
      </div>
      { displayParents(origins.parents) }
    </div>
  );
}
