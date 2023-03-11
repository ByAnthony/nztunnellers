import {
  Date, Death, EmbarkationUnit, Enlistment, PostWarDeath, TransferredTo, Transport,
} from '../../types/tunneller';
import { Name } from '../../types/roll';
import STYLES from './ProfileOverview.module.scss';

type Props = {
    id: number,
    name: Name,
    enlistment: Enlistment,
    embarkation: EmbarkationUnit,
    transportUk: Transport,
    transferred: TransferredTo | null,
    deathDuringWar: Death | null,
    deathAfterWar: PostWarDeath | null,
}

export function ProfileOverview({
  id,
  name,
  enlistment,
  embarkation,
  transportUk,
  transferred,
  deathDuringWar,
  deathAfterWar,
}: Props) {
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
      return `, on ${transportUk.departureDate.dayMonth}.`;
    }
    return `, on ${transportUk.departureDate.dayMonth} ${transportUk.departureDate.year}.`;
  };

  const isTransferred = (transferredData: TransferredTo | null) => {
    if (transferredData) {
      return ` After serving in the war underground in the north of France, he was transferred to the ${transferred?.unit}, on ${transferred?.date.dayMonth} ${transferred?.date.year}.`;
    }
    return null;
  };

  const death = (deathWar: Death | null, deathNotWar: PostWarDeath | null) => {
    if (deathNotWar) {
      return !deathNotWar.date.dayMonth
        ? ` ${firstName} died in ${deathNotWar.date.year}.`
        : ` ${firstName} died on ${deathNotWar.date.dayMonth} ${deathNotWar.date.year}.`;
    }
    if (deathWar) {
      if (deathWar.cause?.type === 'Killed in action') {
        return ` He was engaged in the war underground in the north of France. ${firstName} was killed in action on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      if (deathWar.cause?.type === 'Died of wounds') {
        return ` He was engaged in the war underground in the north of France.  Wounded in action, ${firstName} died on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      if (deathWar.cause?.type === 'Died of disease') {
        return ` He was engaged in the war underground in the north of France.  ${firstName} died of disease on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      return ` He was engaged in the war underground in the north of France. ${firstName} died on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
    }
    return null;
  };

  const isMichaelTobin = (idTunneller: number) => {
    if (idTunneller === 848) {
      return ' He was the first New Zealand soldier to died on the Western Front.';
    }
    return null;
  };

  return (
    <div className={STYLES.description}>
      <h2>Overview</h2>
      <p>
        {`${firstName} ${name.surname}`}
        {enlistedOrPosted(
          enlistment.date,
          enlistment.transferredToTunnellers?.date,
          enlistment.transferredToTunnellers?.postedFrom,
        )}
        {`He left New Zealand with the ${embarkation.detachment} of the Tunnelling Company`}
        {yearOrFullDate(
          enlistment.date,
          enlistment.transferredToTunnellers?.date,
          transportUk.departureDate,
        )}
        {isTransferred(transferred)}
        {death(deathDuringWar, deathAfterWar)}
        {isMichaelTobin(id)}
      </p>
    </div>
  );
}
