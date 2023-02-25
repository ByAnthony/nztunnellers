import type { Summary } from '../../types/tunneller';
import STYLES from './ProfileHowToCite.module.scss';

type Props = {
    id: number,
    summary: Summary,
}

const today = new Date();

export function ProfileHowToCite({ id, summary }: Props) {
  const displayBirthDeathDates = (birth: string | undefined, death: string | undefined) => (death ? `${birth}-${death}` : `${birth}-†?`);
  return (
    <div className={STYLES.howtocite}>
      <h3>How to cite this page</h3>
      <p>
        Anthony Byledbal, &lsquo;
        { summary.name.forename }
        {' '}
        { summary.name.surname }
        {' '}
        (
        { displayBirthDeathDates(summary.birth, summary.death) }
        )&rsquo;,
        {' '}
        <em>New Zealand Tunnellers Website</em>
        {', '}
        {today.getFullYear()}
        {' '}
        (2009), Accessed:&nbsp;
        {today.toLocaleDateString()}
        . URL:&nbsp;https://www.nztunnellers.com/roll/
        {id}
        .
      </p>
    </div>
  );
}
