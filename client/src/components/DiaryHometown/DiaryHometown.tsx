import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type props = {
  residence: string | null,
}

export function DiaryHometown({ residence }: props) {
  return residence
    ? (
      <div className={STYLES['halfwidth-cards-container']}>
        <div className={STYLES['halfwidth-main-card']}>
          <span>Live</span>
        </div>
        <div className={STYLES['halfwidth-secondary-card']}>
          <div className={STYLES['halfwidth-secondary-card-title']}><p>Hometown</p></div>
          <div><span>{ residence }</span></div>
        </div>
      </div>
    )
    : null;
}
