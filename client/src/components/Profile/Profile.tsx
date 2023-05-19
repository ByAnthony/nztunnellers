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
  const tunnellerId = Number(id);
  const {
    data, error, isLoading, isSuccess,
  } = useGetTunnellerByIdQuery(tunnellerId);

  const displayBirthDeathDates = (
    birth: string,
    death: string | null,
  ) => (death ? `${birth} - ${death}` : `${birth} - †?`);

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
          <div className={STYLES.header}>
            <div className={STYLES.link}>
              <a href="/tunnellers">The Tunnellers</a>
              <span>/</span>
              {`${data.summary.name.forename} ${data.summary.name.surname}`}
            </div>
            <h1>
              <span className={STYLES.forename}>{ data.summary.name.forename }</span>
              <span className={STYLES.surname}>{ data.summary.name.surname }</span>
            </h1>
            <p className={STYLES.dates}>
              { displayBirthDeathDates(data.summary.birth, data.summary.death) }
            </p>
          </div>
          <div className={STYLES.profile}>
            <div>
              <div className={STYLES.summary}>
                <ProfileSummary
                  embarkationUnit={data.militaryYears.embarkationUnit}
                  enlistment={data.militaryYears.enlistment}
                  image={data.image}
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
              <ProfileHowToCite id={tunnellerId} summary={data.summary} />
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
