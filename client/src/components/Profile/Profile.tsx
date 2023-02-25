import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { ProfileHowToCite } from '../ProfileHowToCite/ProfileHowToCite';
import { ProfileDescription } from '../ProfileDescription/ProfileDescription';
import { ProfileEnlistment } from '../ProfileEnlistment/ProfileEnlistment';
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
          <ProfileDescription
            name={data.summary.name}
            enlistment={data.militaryYears.enlistment}
            embarkation={data.militaryYears.embarkationUnit}
            transportUk={data.militaryYears.transportUk}
          />
          <ProfileEnlistment origins={data.origins} />
          <ProfileSources sources={data.sources} />
          <ProfileHowToCite id={Number(id)} summary={data.summary} />
        </div>
        )}
      </>
    );
  }
  return null;
}
