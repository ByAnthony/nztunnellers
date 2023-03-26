import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { Menu } from '../Menu/Menu';
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
        <Menu />
        { isLoading }
        { isSuccess && (
        <div className={STYLES['profile-container']}>
          <div className={STYLES['sticky-card']}>
            <div className={STYLES.summary}>
              <ProfileSummary
                summary={data.summary}
                embarkationUnit={data.militaryYears.embarkationUnit}
                enlistment={data.militaryYears.enlistment}
              />
            </div>
          </div>
          <div>
            <ProfileOverview
              id={data.id}
              name={data.summary.name}
              militaryYears={data.militaryYears}
            />
            <ProfileDiary
              tunnellerId={data.id}
              origins={data.origins}
              preWarYears={data.preWarYears}
              militaryYears={data.militaryYears}
              postWarYears={data.postServiceYears}
            />
            <ProfileSources sources={data.sources} />
            <ProfileHowToCite id={Number(id)} summary={data.summary} />
          </div>
        </div>
        )}
      </>
    );
  }
  return null;
}
