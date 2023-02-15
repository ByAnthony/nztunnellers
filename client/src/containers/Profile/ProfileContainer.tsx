import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { ProfileSummary } from '../../components/ProfileSummary/ProfileSummary';
import STYLES from './ProfileContainer.module.scss';

export function ProfileContainer() {
  const { id } = useParams();
  const { data, isLoading, isSuccess } = useGetTunnellerByIdQuery(Number(id!));

  if (data) {
    return (
      <>
        { isLoading }
        { isSuccess && (
        <div className={STYLES['profile-container']}>
          <ProfileSummary summary={data.summary} />
        </div>
        )}
      </>
    );
  }
  return null;
}
