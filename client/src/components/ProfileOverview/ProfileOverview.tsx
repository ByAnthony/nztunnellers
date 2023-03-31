import {
  Date, MilitaryYears,
} from '../../types/tunneller';
import { Name } from '../../types/roll';
import STYLES from './ProfileOverview.module.scss';

type props = {
    id: number,
    name: Name,
    militaryYears: MilitaryYears,
}

export function ProfileOverview({
  id,
  name,
  militaryYears,
}: props) {
  const forename = name.forename.split(' ');
  const firstName = forename[0];

  const enlistedOrPosted = (
    enlisted: Date | undefined,
    postedDate: Date | undefined,
    postedFrom: string | undefined,
  ) => (enlisted !== null
    ? (` enlisted on ${enlisted?.dayMonth} ${enlisted?.year}. `)
    : (` was posted to the Tunnellers on ${postedDate?.dayMonth} ${postedDate?.year} from the ${postedFrom}. `));

  const isMichaelTobin = (idTunneller: number, tunnellerName: Name) => {
    if (idTunneller === 848
        && tunnellerName.forename === 'Michael'
        && tunnellerName.surname === 'Tobin'
    ) {
      return ' He was the first New Zealand soldier to die on the Western Front.';
    }
    return null;
  };

  return (
    <div className={STYLES.description}>
      <p>
        {`${firstName} ${name.surname}`}
        {enlistedOrPosted(
          militaryYears.enlistment.date,
          militaryYears.enlistment.transferredToTunnellers?.date,
          militaryYears.enlistment.transferredToTunnellers?.postedFrom,
        )}
        {isMichaelTobin(id, name)}
      </p>
    </div>
  );
}
