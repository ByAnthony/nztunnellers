import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { ProfileHowToCite } from '../ProfileHowToCite/ProfileHowToCite';
import { ProfileOverview } from '../ProfileOverview/ProfileOverview';
import { ProfileDiary } from '../ProfileDiary/ProfileDiary';
import { ProfileSources } from '../ProfileSources/ProfileSources';
import { ProfileSummary } from '../ProfileSummary/ProfileSummary';
import STYLES from './Profile.module.scss';

export function Profile() {
  const { id } = useParams();
  const {
    data, error, isLoading, isSuccess,
  } = useGetTunnellerByIdQuery(Number(id!));

  if (data) {
    return (
      <>
        {error && (
        <div className={STYLES['profile-container']}>
          <p>An error occured</p>
        </div>
        )}
        { isLoading }
        { isSuccess && (
        <div className={STYLES['profile-container']}>
          <ProfileSummary
            summary={data.summary}
            embarkationUnit={data.militaryYears.embarkationUnit}
            enlistment={data.militaryYears.enlistment}
          />
          <ProfileOverview
            name={data.summary.name}
            enlistment={data.militaryYears.enlistment}
            embarkation={data.militaryYears.embarkationUnit}
            transportUk={data.militaryYears.transportUk}
            deathDuringWar={data.militaryYears.endOfService.deathWar}
            deathAfterWar={data.postServiceYears.death}
          />
          <ProfileDiary
            origins={data.origins}
            preWarYears={data.preWarYears}
            militaryYears={data.militaryYears}
            postWarYears={data.postServiceYears}
          />
          <ProfileSources sources={data.sources} />
          <ProfileHowToCite id={Number(id)} summary={data.summary} />
        </div>
        )}
      </>
    );
  }
  return null;
}
