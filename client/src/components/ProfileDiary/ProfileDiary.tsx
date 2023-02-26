import { Birth } from '../../types/tunneller';
import STYLES from './ProfileDiary.module.scss';

type Props = {
  born: Birth;
}

export function ProfileDiary({ born }: Props) {
  return (
    <div className={STYLES.timeline}>
      <h2>Diary</h2>
      <div>
        {born.date.dayMonth}
      </div>
    </div>
  );
}
