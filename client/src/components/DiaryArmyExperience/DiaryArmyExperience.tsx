import { ArmyExperience } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';
import STYLES_WWI from './DiaryArmyExperience.module.scss';

type props = {
  tunnellerId: number,
  armyExperience: ArmyExperience[],
}

export function ArmyExperienceList({ militaryExperience }:
  {militaryExperience: ArmyExperience[] | []}) {
  if (militaryExperience.length > 0) {
    return (
      <>
        {militaryExperience.map((experience) => {
          const displayDurationAndCountry = () => {
            const isUk = (country: string) => (country === 'United Kingdom' ? `the ${country}` : country);
            if (experience.duration !== null && experience.country !== null) {
              return <p>{`${experience.duration} in ${isUk(experience.country)}`}</p>;
            }
            if (experience.duration !== null && experience.country === null) {
              return <p>{experience.duration}</p>;
            }
            if (experience.duration === null && experience.country !== null) {
              return <p>{experience.country}</p>;
            }
            return null;
          };

          if (experience.unit !== 'Other' && experience.conflict !== null) {
            return (
              <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
                <p>{experience.conflict}</p>
                <span>{ experience.unit }</span>
              </li>
            );
          }

          if (experience.unit === 'Other') {
            if (experience.conflict !== null && experience.duration === null) {
              return (
                <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
                  <span>{experience.conflict}</span>
                </li>
              );
            }
            return (
              <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
                <span>{experience.conflict}</span>
                <p>{experience.duration}</p>
              </li>
            );
          }
          return (
            <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
              <span>{ experience.unit }</span>
              { displayDurationAndCountry() }
            </li>
          );
        })}
      </>
    );
  }
  return null;
}

export function DiaryArmyExperience({ tunnellerId, armyExperience }: props) {
  return (
    <>
      <h2>Army Experience</h2>
      <ArmyExperienceList militaryExperience={armyExperience} />
      <a href={`/tunnellers/${tunnellerId}/wwi-timeline`} className={STYLES_WWI['war-service']} aria-label="Open the World War I timeline.">
        <div>
          <p>World War I (1914-1918)</p>
          <span>New Zealand Tunnellers</span>
        </div>
        <div className={STYLES['arrow-right']}>&rarr;</div>
      </a>
    </>
  );
}
