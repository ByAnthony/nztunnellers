import type { Summary } from '../../types/tunneller';
import { today } from '../../utils/utils';
import STYLES from './ProfileHowToCite.module.scss';

type props = {
  id: number;
  summary: Summary;
};

export function ProfileHowToCite({ id, summary }: props) {
  const displayBirthDeathDates = (birth: string, death: string | null) => (death ? `${birth}-${death}` : `${birth}-†?`);
  return (
    <div className={STYLES.howtocite}>
      <h3>How to cite this page</h3>
      <p>
        {`Anthony Byledbal, "${summary.name.forename} ${summary.name.surname} `}
        {`(${displayBirthDeathDates(summary.birth, summary.death)})", `}
        <em>New Zealand Tunnellers Website</em>
        {`, ${today.getFullYear()} (2009), Accessed: `}
        {`${today.toLocaleDateString('en-NZ', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        })}. `}
        {`URL: www.nztunnellers.com/tunnellers/${id}.`}
      </p>
    </div>
  );
}
