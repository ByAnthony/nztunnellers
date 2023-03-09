import { ArmyExperience } from '../../types/tunneller';
import STYLES from '../ProfileDiary/ProfileDiary.module.scss';
import STYLES_WWI from './DiaryArmyExperience.module.scss';

type Props = {
    armyExperience: ArmyExperience[],
}

export function DiaryArmyExperience({ armyExperience }: Props) {
  const displayArmyExperience = (militaryExperience: ArmyExperience[] | []) => {
    const displayExperience = () => militaryExperience.map((experience) => {
      const displayConflict = experience.conflict !== null ? experience.conflict : null;
      const displayDuration = experience.duration !== null ? experience.duration : null;
      const displayCountry = experience.country !== null ? experience.country : null;

      const displayDurationAndCountry = () => {
        if (experience.duration !== null && experience.country !== null) {
          return `${displayDuration} in ${displayCountry}`;
        }
        if (experience.duration !== null && experience.country === null) {
          return displayDuration;
        }
        if (experience.duration === null && experience.country !== null) {
          return displayCountry;
        }
        return null;
      };

      if (experience.unit === 'Other') {
        return (
          <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
            <p>{ displayConflict }</p>
            <p>{ displayDuration }</p>
          </li>
        );
      }

      if (experience.unit !== 'Other' && experience.conflict !== null) {
        return (
          <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
            <p>{ displayConflict }</p>
            <span>{ experience.unit }</span>
            <p>{ displayDuration }</p>
          </li>
        );
      }

      if (experience.unit !== 'Other' && experience.conflict === null) {
        return (
          <li className={STYLES['fullwidth-secondary-card']} key={experience.unit}>
            <span>{ experience.unit }</span>
            <p>{ displayDurationAndCountry() }</p>
          </li>
        );
      }

      return null;
    });

    if (armyExperience.length > 0) {
      return (
        <>
          { displayExperience() }
        </>
      );
    }
    return null;
  };

  return (
    <>
      <div className={STYLES['fullwidth-main-card']}>
        <span>Army Experience</span>
      </div>
      { displayArmyExperience(armyExperience) }
      <div className={STYLES_WWI['war-service']}>
        <div>
          <p>World War I (1914-1918)</p>
          <span>New Zealand Engineers Tunnelling Company</span>
        </div>
        <div className={STYLES.arrow}>&rarr;</div>
      </div>
    </>
  );
}
