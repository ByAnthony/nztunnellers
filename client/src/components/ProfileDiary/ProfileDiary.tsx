import {
  MilitaryYears,
  Origins, PostServiceYears, PreWayYears,
} from '../../types/tunneller';
import { DiaryArmyExperience } from '../DiaryArmyExperience/DiaryArmyExperience';
import { DiaryArrivedInNz } from '../DiaryArrivedInNz/DiaryArrivedInNz';
import { DiaryBirth } from '../DiaryBirthInfo/DiaryBirthInfo';
import { DiaryDied } from '../DiaryDied/DiaryDied';
import { DiaryHometown } from '../DiaryHometown/DiaryHometown';
import { DiaryLife } from '../DiaryLife/DiaryLife';
import { DiaryParents } from '../DiaryParents/DiaryParents';
import { DiaryWork } from '../DiaryWork/DiaryWork';
import STYLES from './ProfileDiary.module.scss';

type Props = {
  origins: Origins,
  preWarYears: PreWayYears,
  militaryYears: MilitaryYears,
  postWarYears: PostServiceYears,
}

export function ProfileDiary({
  origins,
  preWarYears,
  militaryYears,
  postWarYears,
}: Props) {
  return (
    <div className={STYLES.diary}>
      <h2>Diary</h2>
      <DiaryBirth birth={origins.birth} />
      <DiaryParents parents={origins.parents} />
      <DiaryArrivedInNz inNzLength={origins.inNzLength} />
      <DiaryHometown residence={preWarYears.residence} />
      <DiaryWork employment={preWarYears.employment} />
      <DiaryLife maritalStatus={preWarYears.maritalStatus} wife={preWarYears.wife} />
      <DiaryArmyExperience armyExperience={preWarYears.armyExperience} />
      <DiaryDied
        warDeath={militaryYears.endOfService.deathWar}
        afterWarDeath={postWarYears.death}
      />
    </div>
  );
}
