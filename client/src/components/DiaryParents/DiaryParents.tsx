import {
  Parent, Parents,
} from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

  type props = {
    parents: Parents;
  }

export function DiaryParents({ parents }: props) {
  const displayParents = (family: Parents) => {
    if (family.mother !== null && family.father !== null) {
      return (
        <>
          <div className={STYLES['fullwidth-main-card']}>
            Parents
          </div>
          <div className={STYLES['halfwidth-cards-container']}>
            <div className={STYLES['halfwidth-secondary-card']}>
              <div className={STYLES['halfwidth-secondary-card-title']}><p>Mother</p></div>
              <div><span>{ family.mother.name }</span></div>
            </div>
            <div className={STYLES['halfwidth-secondary-card']}>
              <div className={STYLES['halfwidth-secondary-card-title']}><p>Father</p></div>
              <div><span>{ family.father.name }</span></div>
            </div>
          </div>
        </>
      );
    }

    const isMotherOrFather = parents.mother ? 'Mother' : 'Father';

    const displayParent = (parent: Parent) => (
      <div className={STYLES['halfwidth-cards-container']}>
        <div className={STYLES['halfwidth-main-card']}>
          <span>Parent</span>
        </div>
        <div className={STYLES['halfwidth-secondary-card']}>
          <div className={STYLES['halfwidth-secondary-card-title']}><p>{ isMotherOrFather }</p></div>
          <div><span>{ parent.name }</span></div>
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

  return (
    <>
      { displayParents(parents) }
    </>
  );
}
