import { ArmyExperience } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';
import STYLES_WWI from './DiaryArmyExperience.module.scss';

type props = {
  tunnellerId: number,
  armyExperience: ArmyExperience[],
}

export function DiaryArmyExperience({ tunnellerId, armyExperience }: props) {
  const displayArmyExperience = (militaryExperience: ArmyExperience[] | []) => {
    const displayExperience = () => militaryExperience.map((experience) => {
      const displayConflict = experience.conflict !== null ? <p>{experience.conflict}</p> : null;
      const isUk = (country: string) => (country === 'United Kingdom' ? `the ${country}` : country);

      const displayDurationAndCountry = () => {
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

      if (experience.unit !== 'Other' && experience.conflict === null) {
        return (
          <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
            <span>{ experience.unit }</span>
            { displayDurationAndCountry() }
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

      if (experience.unit !== 'Other' && experience.conflict !== null) {
        return (
          <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
            { displayConflict }
            <span>{ experience.unit }</span>
          </li>
        );
      }

      return null;
    });

    if (armyExperience.length > 0) {
      return (
        displayExperience()
      );
    }
    return null;
  };

  return (
    <>
      <h2>Army Experience</h2>
      { displayArmyExperience(armyExperience) }
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
