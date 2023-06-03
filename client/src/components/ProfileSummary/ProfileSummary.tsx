import type { EmbarkationUnit, Enlistment, Image } from '../../types/tunneller';
import STYLES from './ProfileSummary.module.scss';

type props = {
    embarkationUnit: EmbarkationUnit,
    enlistment: Enlistment,
    image: Image | null,
}

function RenderImage({ imageUrl }: {imageUrl: string | undefined}) {
  return imageUrl ? (
    <div className={STYLES['image-card']}>
      <img src={`/images/roll/tunnellers/${imageUrl}`} alt="" />
    </div>
  ) : null;
}

function RenderUnit({ unit, section }:
  {unit: string,
  section: string | null,}) {
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
}

export function ProfileSummary({ embarkationUnit, enlistment, image }: props) {
  return (
    <div className={STYLES.overview}>
      <RenderImage imageUrl={image?.url} />
      <RenderUnit unit={embarkationUnit.detachment} section={embarkationUnit.section} />
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
