import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { ProfileHeader } from '../../components/ProfileHeader/ProfileHeader';
import STYLES from './ProfileContainer.module.scss';

export function ProfileContainer() {
  const { id } = useParams();
  const { data, isLoading, isSuccess } = useGetTunnellerByIdQuery(Number(id!));
  function getSafe(fn: Function, defaultVal: unknown) {
    try {
      return fn();
    } catch (e) {
      return defaultVal;
    }
  }

  if (data) {
    return (
      <>
        { isLoading }
        { isSuccess && (
        <div className={STYLES['profile-container']}>
          <ProfileHeader
            serial={data.serial}
            name={data.name}
            birth={data.origins.birth.date.year}
            death={getSafe(() => data.postServiceYears.death.date.year, null)}
          />
        </div>
        )}
      </>
    );
  }
  return null;
}
