import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type Props = {
    inNzLength: string | null,
}

export function DiaryArrivedInNz({ inNzLength }: Props) {
  const displayImmigrationYear = (immigrationYear: string) => (
    <div className={STYLES['fullwidth-secondary-card']}>
      <p>Arrived in New Zealand</p>
      <span>{ immigrationYear }</span>
    </div>
  );

  return (
    <div>
      { inNzLength ? displayImmigrationYear(inNzLength) : null }
    </div>
  );
}
