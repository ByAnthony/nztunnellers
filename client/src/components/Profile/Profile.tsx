import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import { Menu } from '../Menu/Menu';
import { ProfileHowToCite } from '../ProfileHowToCite/ProfileHowToCite';
import { ProfileDiary } from '../ProfileDiary/ProfileDiary';
import { ProfileSources } from '../ProfileSources/ProfileSources';
import { ProfileSummary } from '../ProfileSummary/ProfileSummary';
import STYLES from './Profile.module.scss';
import { Footer } from '../Footer/Footer';

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
          <div>
            <div className={STYLES['profile-summary']}>
              <ProfileSummary
                summary={data.summary}
                embarkationUnit={data.militaryYears.embarkationUnit}
                enlistment={data.militaryYears.enlistment}
              />
            </div>
          </div>
          <div>
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
        <Footer />
      </>
    );
  }
  return null;
}
