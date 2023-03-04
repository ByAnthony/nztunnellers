import {
  Date, Origins, Parent, Parents,
} from '../../types/tunneller';
import STYLES from './ProfileDiary.module.scss';

type Props = {
  origins: Origins;
}

export function ProfileDiary({ origins }: Props) {
  const displayBirthCountry = (country: string | null) => (
    country !== null ? (
      <p>
        {`Born in ${country}`}
      </p>
    ) : <p>Born</p>
  );

  const displayBirthDate = (birth: Date) => (
    birth.dayMonth !== null ? (
      `${birth.dayMonth} ${birth.year}`
    ) : `${birth.year}`
  );

  const displayBirthInfo = (birthCountry: string | null, birthDate: Date) => (
    <div className={STYLES['fullwidth-title-card']}>
      { displayBirthCountry(birthCountry) }
      { displayBirthDate(birthDate) }
    </div>
  );

  const displayParents = (parents: Parents) => {
    if (parents.mother !== null && parents.father !== null) {
      return (
        <>
          <div className={STYLES['fullwidth-title-card']}>
            Parents
          </div>
          <div className={STYLES['card-container']}>
            <div className={STYLES['parents-card']}>
              <div className={STYLES['parents-card-title']}><p>Mother</p></div>
              <div>{ parents.mother.name }</div>
            </div>
            <div className={STYLES['parents-card']}>
              <div className={STYLES['parents-card-title']}><p>Father</p></div>
              <div>{ parents.father.name }</div>
            </div>
          </div>
        </>
      );
    }

    const isMotherOrFather = parents.mother ? 'Mother' : 'Father';

    const displayParent = (parent: Parent) => (
      <div className={STYLES['card-container']}>
        <div className={STYLES['parent-title-card']}>
          Parent
        </div>
        <div className={STYLES['parent-card']}>
          <div className={STYLES['parents-card-title']}><p>{ isMotherOrFather }</p></div>
          <div>{ parent.name }</div>
        </div>
      </div>
    );

    if (parents.mother !== null && parents.father === null) {
      return displayParent(parents.mother);
    }
    if (parents.mother === null && parents.father !== null) {
      return displayParent(parents.father);
    }
    return null;
  };

  const displayImmigrationYear = (inNzLength: string) => (
    <div className={STYLES['fullwidth-title-card']}>
      <p>Arrived in New Zealand</p>
      { inNzLength }
    </div>
  );

  return (
    <div className={STYLES.diary}>
      <h2>Diary</h2>
      { displayBirthInfo(origins.birth.country, origins.birth.date) }
      { displayParents(origins.parents) }
      { origins.inNzLength ? displayImmigrationYear(origins.inNzLength) : null }
    </div>
  );
}
