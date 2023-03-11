import {
  Date, Death, EmbarkationUnit, Enlistment, PostWarDeath, Transport,
} from '../../types/tunneller';
import { Name } from '../../types/roll';
import STYLES from './ProfileOverview.module.scss';

type Props = {
    name: Name,
    enlistment: Enlistment,
    embarkation: EmbarkationUnit,
    transportUk: Transport,
    deathDuringWar: Death | null,
    deathAfterWar: PostWarDeath | null,
}

export function ProfileOverview({
  name,
  enlistment,
  embarkation,
  transportUk,
  deathDuringWar,
  deathAfterWar,
}: Props) {
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

  const death = (deathWar: Death | null, deathNotWar: PostWarDeath | null) => {
    if (deathNotWar) {
      return !deathNotWar.date.dayMonth
        ? ` He died in ${deathNotWar.date.year}.`
        : ` He died on ${deathNotWar.date.dayMonth} ${deathNotWar.date.year}.`;
    }
    if (deathWar) {
      if (deathWar.cause?.type === 'Killed in action') {
        return ` He was killed in action on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      if (deathWar.cause?.type === 'Died of wounds') {
        return ` Wounded in action, he died on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
      }
      return ` He died on ${deathWar.date.dayMonth} ${deathWar.date.year}.`;
    }
    return null;
  };

  return (
    <div className={STYLES.description}>
      <h2>Overview</h2>
      <p>
        {`${name.forename} ${name.surname}`}
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
        {death(deathDuringWar, deathAfterWar)}
      </p>
    </div>
  );
}
