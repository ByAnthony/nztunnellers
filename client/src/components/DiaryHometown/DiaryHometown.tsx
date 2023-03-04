import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type Props = {
  residence: string | null,
}

export function DiaryHometown({ residence }: Props) {
  const displayHometown = (town: string | null) => (
    town
      ? (
        <>
          <div className={STYLES['fullwidth-main-card']}>
            <span>Live</span>
          </div>
          <div className={STYLES['fullwidth-secondary-card']}>
            <p>Hometown</p>
            <span>{ town }</span>
          </div>
        </>
      )
      : null
  );

  return (
    <>
      { displayHometown(residence) }
    </>
  );
}
