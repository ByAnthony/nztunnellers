import { displayBirthDeathDates } from '../../utils/utils';
import type { Summary } from '../../types/tunneller';
import STYLES from './ProfileHowToCite.module.scss';

type Props = {
  id: number;
  summary: Summary;
  date: Date;
};

export function ProfileHowToCite({ id, summary, date }: Props) {
  return (
    <div className={STYLES.howtocite}>
      <h3>How to cite this page</h3>
      <p>
        Anthony Byledbal, &ldquo;
        {`${summary.name.forename} ${summary.name.surname} `}
        {`(${displayBirthDeathDates(summary.birth, summary.death)})`}
        &ldquo;,
        <em> New Zealand Tunnellers Website</em>
        {`, ${date.getFullYear()} (2009), Accessed: `}
        {`${date.toLocaleDateString('en-NZ', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        })}. `}
        {`URL: www.nztunnellers.com/tunnellers/${id}.`}
      </p>
    </div>
  );
}
