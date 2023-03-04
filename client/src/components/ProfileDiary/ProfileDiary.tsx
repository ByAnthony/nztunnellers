import {
  Origins,
} from '../../types/tunneller';
import { DiaryArrivedInNz } from '../DiaryArrivedInNz/DiaryArrivedInNz';
import { DiaryBirth } from '../DiaryBirthInfo/DiaryBirthInfo';
import { DiaryParents } from '../DiaryParents/DiaryParents';
import STYLES from './ProfileDiary.module.scss';

type Props = {
  origins: Origins;
}

export function ProfileDiary({ origins }: Props) {
  return (
    <div className={STYLES.diary}>
      <h2>Diary</h2>
      <DiaryBirth birth={origins.birth} />
      <DiaryParents parents={origins.parents} />
      <DiaryArrivedInNz inNzLength={origins.inNzLength} />
    </div>
  );
}
