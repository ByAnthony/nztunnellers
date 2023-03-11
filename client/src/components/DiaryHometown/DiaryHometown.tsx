import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type Props = {
  residence: string | null,
}

export function DiaryHometown({ residence }: Props) {
  const displayHometown = (town: string | null) => (
    town
      ? (
        <div className={STYLES['halfwidth-cards-container']}>
          <div className={STYLES['halfwidth-main-card']}>
            <span>Live</span>
          </div>
          <div className={STYLES['halfwidth-secondary-card']}>
            <div className={STYLES['halfwidth-secondary-card-title']}><p>Hometown</p></div>
            <div><span>{ town }</span></div>
          </div>
        </div>
      )
      : null
  );

  return (
    <>
      { displayHometown(residence) }
    </>
  );
}
