import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type props = {
    inNzLength: string | null,
}

export function DiaryArrivedInNz({ inNzLength }: props) {
  const displayImmigrationYear = (immigrationYear: string) => (
    <div className={STYLES['fullwidth-main-card']}>
      <p>Settled in New Zealand</p>
      <span>{ immigrationYear }</span>
    </div>
  );

  return (
    inNzLength ? displayImmigrationYear(inNzLength) : null
  );
}
