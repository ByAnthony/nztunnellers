import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type props = {
    inNzLength: string | null,
}

export function DiaryArrivedInNz({ inNzLength }: props) {
  return (
    inNzLength ? (
      <div className={STYLES['fullwidth-main-card']}>
        <p>Settled in New Zealand</p>
        <span>{ inNzLength }</span>
      </div>
    ) : null
  );
}
