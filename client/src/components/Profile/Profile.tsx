import { useParams } from 'react-router-dom';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';

import { displayBirthDeathDates } from '../../utils/utils';
import { today } from '../../utils/date-utils';

import { Footer } from '../Footer/Footer';
import { HowToCite } from '../HowToCite/HowToCite';
import { Menu } from '../Menu/Menu';
import { ProfileDiary } from '../ProfileDiary/ProfileDiary';
import { ProfileImageSource } from '../ProfileImageSource/ProfileImageSource';
import { ProfileSources } from '../ProfileSources/ProfileSources';
import { ProfileSummary } from '../ProfileSummary/ProfileSummary';
import { Title } from '../Title/Title';

import STYLES from './Profile.module.scss';

export function Profile() {
  const { id } = useParams();
  const tunnellerId = Number(id);
  const {
    data, error, isLoading, isSuccess,
  } = useGetTunnellerByIdQuery(tunnellerId);

  if (data) {
    return (
      <>
        {error && (
        <div className={STYLES.profile}>
          <p>An error occured</p>
        </div>
        )}
        <Menu />
        { isLoading }
        { isSuccess && (
        <>
          <div className={STYLES.container}>
            <div className={STYLES.header}>
              <div className={STYLES.link}>
                <a href="/tunnellers">Tunnellers</a>
              </div>
              <Title
                name={data.summary.name}
                subTitle={displayBirthDeathDates(data.summary.birth, data.summary.death)}
              />
            </div>
          </div>
          <div className={STYLES.profile}>
            <div className={STYLES['flex-summary']}>
              <div className={STYLES.summary}>
                <ProfileSummary
                  summary={data.summary}
                  embarkationUnit={data.militaryYears.embarkationUnit}
                  enlistment={data.militaryYears.enlistment}
                  image={data.image}
                />
              </div>
            </div>
            <div className={STYLES['flex-diary']}>
              <ProfileDiary
                tunnellerId={data.id}
                origins={data.origins}
                preWarYears={data.preWarYears}
                militaryYears={data.militaryYears}
                postWarYears={data.postServiceYears}
              />
              <ProfileSources sources={data.sources} />
              <ProfileImageSource source={data.image?.source} />
              <HowToCite id={data.id} summary={data.summary} today={today} />
            </div>
          </div>
        </>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
