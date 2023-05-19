import type { EmbarkationUnit, Enlistment, Image } from '../../types/tunneller';
import STYLES from './ProfileSummary.module.scss';

type props = {
    embarkationUnit: EmbarkationUnit,
    enlistment: Enlistment,
    image: Image | null,
}

export function ProfileSummary({ embarkationUnit, enlistment, image }: props) {
  const displayImage = (imageUrl: string | undefined) => (
    imageUrl ? (
      <div className={STYLES['image-card']}>
        <img src={`/images/roll/tunnellers/${image?.url}`} alt="" />
      </div>
    ) : null);

  const displayUnit = (
    unit: string,
    section: string | null,
  ) => {
    if (unit === 'Main Body' && section) {
      return (
        <>
          <div className={STYLES['fullwidth-main-card']}>
            <p>Unit</p>
            <span>{ unit }</span>
          </div>
          <div className={STYLES['fullwidth-main-card']}>
            <p>Section</p>
            <span>{ section }</span>
          </div>
        </>
      );
    }
    return (
      <div className={STYLES['fullwidth-main-card']}>
        <p>Unit</p>
        <span>{ unit }</span>
      </div>
    );
  };

  return (
    <div className={STYLES.overview}>
      { displayImage(image?.url) }
      { displayUnit(embarkationUnit.detachment, embarkationUnit.section) }
      <div className={STYLES['halfwidth-cards-container']}>
        <div className={STYLES['halfwidth-secondary-card']}>
          <div className={STYLES['halfwidth-secondary-card-title']}><p>Rank</p></div>
          <div><span>{ enlistment.rank }</span></div>
        </div>
        <div className={STYLES['halfwidth-secondary-card']}>
          <div className={STYLES['halfwidth-secondary-card-title']}><p>Serial</p></div>
          <div><span>{ enlistment.serial }</span></div>
        </div>
      </div>
    </div>
  );
}
