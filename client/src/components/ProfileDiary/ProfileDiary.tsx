import {
  Origins, PreWayYears,
} from '../../types/tunneller';
import { DiaryArrivedInNz } from '../DiaryArrivedInNz/DiaryArrivedInNz';
import { DiaryBirth } from '../DiaryBirthInfo/DiaryBirthInfo';
import { DiaryHometown } from '../DiaryHometown/DiaryHometown';
import { DiaryParents } from '../DiaryParents/DiaryParents';
import STYLES from './ProfileDiary.module.scss';

type Props = {
  origins: Origins;
  preWarYears: PreWayYears
}

export function ProfileDiary({
  origins,
  preWarYears,
}: Props) {
  return (
    <div className={STYLES.diary}>
      <h2>Diary</h2>
      <DiaryBirth birth={origins.birth} />
      <DiaryParents parents={origins.parents} />
      <DiaryArrivedInNz inNzLength={origins.inNzLength} />
      <DiaryHometown hometown={preWarYears.residence} />
    </div>
  );
}
