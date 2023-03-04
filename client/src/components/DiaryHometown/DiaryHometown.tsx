import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type Props = {
    hometown: string | null,
}

export function DiaryHometown({ hometown }: Props) {
  const displayHometown = (town: string | null) => (
    town
      ? (
        <div className={STYLES['fullwidth-main-card']}>
          <p>Hometown</p>
          <span>{ town }</span>
        </div>
      )
      : null
  );

  return (
    <>
      { displayHometown(hometown) }
    </>
  );
}
