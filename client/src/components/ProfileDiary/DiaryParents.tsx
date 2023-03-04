import {
  Parent, Parents,
} from '../../types/tunneller';
import STYLES from './ProfileDiary.module.scss';

  type Props = {
    parents: Parents;
  }

export function DiaryParents({ parents }: Props) {
  const displayParents = (family: Parents) => {
    if (family.mother !== null && family.father !== null) {
      return (
        <>
          <div className={STYLES['fullwidth-card']}>
            Parents
          </div>
          <div className={STYLES['cards-container']}>
            <div className={STYLES['parents-card']}>
              <div className={STYLES['parents-card-title']}><p>Mother</p></div>
              <div><span>{ family.mother.name }</span></div>
            </div>
            <div className={STYLES['parents-card']}>
              <div className={STYLES['parents-card-title']}><p>Father</p></div>
              <div><span>{ family.father.name }</span></div>
            </div>
          </div>
        </>
      );
    }

    const isMotherOrFather = parents.mother ? 'Mother' : 'Father';

    const displayParent = (parent: Parent) => (
      <div className={STYLES['cards-container']}>
        <div className={STYLES['parent-title-card']}>
          Parent
        </div>
        <div className={STYLES['parent-card']}>
          <div className={STYLES['parents-card-title']}><p>{ isMotherOrFather }</p></div>
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
