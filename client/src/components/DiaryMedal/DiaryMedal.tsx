import { Medal } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';
import OTHER_MEDALS_STYLES from './DiaryMedal.module.scss';

type Props = {
    medals: Medal[] | [];
}

function BritishWarAndVictoryMedals({ medalsList }: {medalsList: Medal[] | []}) {
  const filteredMedals = medalsList.filter((medal) => medal.name === 'British War Medal' || medal.name === 'Victory Medal');

  if (filteredMedals.length > 0) {
    return (
      <div className={STYLES['halfwidth-cards-container']}>
        {filteredMedals.map((medal) => (
          <div key={filteredMedals.indexOf(medal)} className={STYLES['halfwidth-secondary-card']}>
            <p><img src={`/images/roll/medals/${medal.image}`} alt={`${medal.name} ribbon`} width={40} /></p>
            <span>{ medal.name }</span>
          </div>
        ))}
      </div>
    );
  }
  return null;
}

function OtherMedals({ medalsList }: {medalsList: Medal[] | []}) {
  const filteredMedals = medalsList.filter((medal) => medal.name !== 'British War Medal' && medal.name !== 'Victory Medal');
  return (
    <>
      {filteredMedals.map((medal) => {
        const displayCountry = (medal.country !== 'United Kingdom') ? `(${medal.country})` : '';
        return (
          <div key={filteredMedals.indexOf(medal)} className={OTHER_MEDALS_STYLES['other-medal']}>
            <p><img src={`/images/roll/medals/${medal.image}`} alt={`${medal.name} ribbon`} width={40} /></p>
            <span>{`${medal.name} ${displayCountry}`}</span>
            <div className={OTHER_MEDALS_STYLES.citation}><span>{`${medal.citation}.`}</span></div>
          </div>
        );
      })}
    </>
  );
}

export function DiaryMedal({ medals }: Props) {
  return (
    <>
      <BritishWarAndVictoryMedals medalsList={medals} />
      <OtherMedals medalsList={medals} />
    </>
  );
}
