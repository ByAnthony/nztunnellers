import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { ProfileHeader } from '../../components/ProfileHeader/ProfileHeader';
import STYLES from './ProfileContainer.module.scss';

export function ProfileContainer() {
  const { id } = useParams();
  const { data } = useGetTunnellerByIdQuery(Number(id!));

  return (
    <div className={STYLES['profile-container']}>
      <ProfileHeader serial={data?.serial} name={data?.name} />
    </div>
  );
}
