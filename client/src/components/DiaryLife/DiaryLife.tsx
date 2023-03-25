import STYLES from '../ProfileDiary/ProfileDiary.module.scss';

type props = {
    maritalStatus: string | null,
    wife: string | null,
}

export function DiaryLife({ maritalStatus, wife }: props) {
  const displayLife = (status: string | null, wifeName: string | null) => {
    if (maritalStatus !== null && wifeName !== null) {
      return (
        <>
          <div className={STYLES['fullwidth-main-card']}>
            Life
          </div>
          <div className={STYLES['halfwidth-cards-container']}>
            <div className={STYLES['halfwidth-secondary-card']}>
              <div className={STYLES['halfwidth-secondary-card-title']}><p>Marital Status</p></div>
              <div><span>{ status }</span></div>
            </div>
            <div className={STYLES['halfwidth-secondary-card']}>
              <div className={STYLES['halfwidth-secondary-card-title']}><p>Wife</p></div>
              <div><span>{ wifeName }</span></div>
            </div>
          </div>
        </>
      );
    }

    const displayMaritalStatus = (statusWithoutWife: string | null) => (
      <div className={STYLES['halfwidth-cards-container']}>
        <div className={STYLES['halfwidth-main-card']}>
          <span>Life</span>
        </div>
        <div className={STYLES['halfwidth-secondary-card']}>
          <div className={STYLES['halfwidth-secondary-card-title']}><p>Marital Status</p></div>
          <div><span>{ statusWithoutWife }</span></div>
        </div>
      </div>
    );

    if (maritalStatus !== null && wifeName === null) {
      return displayMaritalStatus(maritalStatus);
    }
    return null;
  };

  return (
    <>
      { displayLife(maritalStatus, wife) }
    </>
  );
}
