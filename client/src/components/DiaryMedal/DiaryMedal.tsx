import { Medal } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';
import OTHER_MEDALS_STYLES from './DiaryMedal.module.scss';

type props = {
    medals: Medal[] | [],
}

function BritishWarAndVictoryMedals({ medalsList }: {medalsList: Medal[] | []}) {
  const filteredMedals = medalsList.filter((medal) => medal.name === 'British War Medal' || medal.name === 'Victory Medal');
  return (
    <>
      {filteredMedals.map((medal) => (
        <div key={filteredMedals.indexOf(medal)} className={STYLES['halfwidth-secondary-card']}>
          <div className={STYLES['halfwidth-secondary-card-title']}><p><img src={`/images/roll/medals/${medal.image}`} alt="" width={40} /></p></div>
          <div><span>{ medal.name }</span></div>
        </div>
      ))}
    </>
  );
}

function OtherMedals({ medalsList }: {medalsList: Medal[] | []}) {
  const filteredMedals = medalsList.filter((medal) => medal.name !== 'British War Medal' && medal.name !== 'Victory Medal');
  return (
    <>
      {filteredMedals.map((medal) => {
        const displayCountry = (medal.country !== 'United Kingdom') ? `(${medal.country})` : '';
        return (
          <div key={filteredMedals.indexOf(medal)} className={OTHER_MEDALS_STYLES['other-medal']}>
            <div><p><img src={`/images/roll/medals/${medal.image}`} alt="" width={40} /></p></div>
            <div><span>{`${medal.name} ${displayCountry}`}</span></div>
            <div className={OTHER_MEDALS_STYLES.citation}><span>{`${medal.citation}.`}</span></div>
          </div>
        );
      })}
    </>
  );
}

export function DiaryMedal({ medals }: props) {
  return (
    <>
      <div className={STYLES['halfwidth-cards-container']}>
        <BritishWarAndVictoryMedals medalsList={medals} />
      </div>
      <OtherMedals medalsList={medals} />
    </>
  );
}
