import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import STYLES from './ProfileContainer.module.scss';
import { ProfileSummary } from '../ProfileSummary/ProfileSummary';

export function ProfileContainer() {
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
          <ProfileSummary summary={data.summary} />
          {/* <ProfileOrigins />
          <ProfilePreWarYears />
          <ProfileMilitaryYears />
          <ProfilePostServiceYears />
          <ProfileSources /> */}
        </div>
        )}
      </>
    );
  }
  return null;
}
