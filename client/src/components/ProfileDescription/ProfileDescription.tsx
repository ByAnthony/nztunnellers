import {
  Date, EmbarkationUnit, Enlistment, Transport,
} from '../../types/tunneller';
import { Name } from '../../types/roll';
import STYLES from './ProfileDescription.module.scss';

type Props = {
    name: Name,
    enlistment: Enlistment,
    embarkation: EmbarkationUnit,
    transportUk: Transport,
}

export function ProfileDescription({
  name,
  enlistment,
  embarkation,
  transportUk,
}: Props) {
  const enlistedOrPosted = (
    enlisted: Date | undefined,
    postedDate: Date | undefined,
    postedFrom: string | undefined,
  ) => (enlisted !== null
    ? (`enlisted on ${enlisted?.dayMonth} ${enlisted?.year}`)
    : (`was posted to the Tunnellers on ${postedDate?.dayMonth} ${postedDate?.year} from the ${postedFrom}`));

  const yearOrFullDate = (
    enlisted: Date | undefined,
    postedDate: Date | undefined,
    transportUkDate: Date | undefined,
  ) => {
    if (enlisted?.year === transportUkDate?.year || postedDate?.year === transportUkDate?.year) {
      return `${transportUk.departureDate.dayMonth}`;
    }
    return `${transportUk.departureDate.dayMonth} ${transportUk.departureDate.year}`;
  };

  return (
    <div className={STYLES.description}>
      <h2>About</h2>
      <p>
        {name.forename}
        {' '}
        {name.surname}
        {' '}
        {enlistedOrPosted(
          enlistment.date,
          enlistment.transferredToTunnellers?.date,
          enlistment.transferredToTunnellers?.postedFrom,
        )}
        {'. He left New Zealand with the '}
        {embarkation.detachment}
        {' of the Tunnelling Company, on '}
        {yearOrFullDate(
          enlistment.date,
          enlistment.transferredToTunnellers?.date,
          transportUk.departureDate,
        )}
        .
      </p>
    </div>
  );
}
