import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
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
          <ProfileSummary summary={data.summary} />
          <ProfileSources sources={data.sources} />
        </div>
        )}
      </>
    );
  }
  return null;
}
