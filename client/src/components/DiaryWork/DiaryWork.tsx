import {
  Employment,
} from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

    type Props = {
        employment: Employment;
    }

export function DiaryWork({ employment }: Props) {
  const displayEmployment = (work: Employment) => {
    if (work.occupation !== null && work.employer !== null) {
      return (
        <>
          <div className={STYLES['fullwidth-main-card']}>
            Work
          </div>
          <div className={STYLES['halfwidth-cards-container']}>
            <div className={STYLES['halfwidth-secondary-card']}>
              <div className={STYLES['halfwidth-secondary-card-title']}><p>Occupation</p></div>
              <div><span>{ work.occupation }</span></div>
            </div>
            <div className={STYLES['halfwidth-secondary-card']}>
              <div className={STYLES['halfwidth-secondary-card-title']}><p>Employer</p></div>
              <div><span>{ work.employer }</span></div>
            </div>
          </div>
        </>
      );
    }

    const displayOccupation = (occupation: string | null) => (
      <div className={STYLES['halfwidth-cards-container']}>
        <div className={STYLES['halfwidth-main-card']}>
          Work
        </div>
        <div className={STYLES['halfwidth-secondary-card']}>
          <div className={STYLES['halfwidth-secondary-card-title']}><p>Occupation</p></div>
          <div><span>{ occupation }</span></div>
        </div>
      </div>
    );

    if (work.occupation !== null && work.employer === null) {
      return displayOccupation(work.occupation);
    }
    return null;
  };

  return (
    <>
      { displayEmployment(employment) }
    </>
  );
}
