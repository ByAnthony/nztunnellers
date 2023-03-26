import {
  Date, Death, MilitaryYears, TransferredTo,
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

  const yearOrFullDate = (
    enlisted: Date | undefined,
    postedDate: Date | undefined,
    transportUkDate: Date | undefined,
  ) => {
    if (enlisted?.year === transportUkDate?.year || postedDate?.year === transportUkDate?.year) {
      return `, on ${militaryYears.transportUk.departureDate.dayMonth}.`;
    }
    return `, on ${militaryYears.transportUk.departureDate.dayMonth} ${militaryYears.transportUk.departureDate.year}.`;
  };

  const isTransferred = (transferredData: TransferredTo | null) => {
    if (transferredData) {
      return ` After serving in the war underground in the north of France,
      he was transferred to the ${militaryYears.endOfService.transferred?.unit}
      on ${militaryYears.endOfService.transferred?.date.dayMonth} ${militaryYears.endOfService.transferred?.date.year}.`;
    }
    return null;
  };

  const death = (deathWar: Death | null) => {
    if (deathWar) {
      if (deathWar.cause?.type === 'Killed in action') {
        return ` He was engaged in the war underground in the north of France.
        ${firstName} was killed in action on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      if (deathWar.cause?.type === 'Died of wounds') {
        return ` He was engaged in the war underground in the north of France.
        Wounded in action, ${firstName} died on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      if (deathWar.cause?.type === 'Died of disease') {
        return ` He was engaged in the war underground in the north of France.
        ${firstName} died of disease on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      return ` He was engaged in the war underground in the north of France.
      ${firstName} died on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
    }
    return null;
  };

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
        {`He left New Zealand with the ${militaryYears.embarkationUnit.detachment} of the Tunnelling Company`}
        {yearOrFullDate(
          militaryYears.enlistment.date,
          militaryYears.enlistment.transferredToTunnellers?.date,
          militaryYears.transportUk.departureDate,
        )}
        {isTransferred(militaryYears.endOfService.transferred)}
        {death(militaryYears.endOfService.deathWar)}
        {isMichaelTobin(id, name)}
      </p>
    </div>
  );
}
