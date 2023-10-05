import { useParams } from 'react-router-dom';
import { HowToCite } from '../HowToCite/HowToCite';
import { today } from '../../utils/date';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';

import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';
import { TimelineEvents } from './TimelineEvents/TimelineEvents';

import STYLES from './Timeline.module.scss';

export function Timeline() {
  const { id } = useParams();
  const tunnellerId = Number(id);
  const {
    data, error, isLoading, isSuccess,
  } = useGetTunnellerByIdQuery(tunnellerId);

  if (data) {
    const { name } = data.summary;
    const { militaryYears, postServiceYears } = data;

    return (
      <>
        {error && (
        <div className={STYLES.timeline}>
          <p>An error occured</p>
        </div>
        )}
        { isLoading }
        <Menu />
        { isSuccess && (
          <>
            <div className={STYLES.timeline}>
              <div className={STYLES.header}>
                <div className={STYLES.link}>
                  <a href="/tunnellers">Tunnellers</a>
                  <span>/</span>
                  <a href={`/tunnellers/${tunnellerId}`}>{`${name.forename} ${name.surname}`}</a>
                </div>
                <div className={STYLES['main-title']}>
                  <h1>
                    <span className={STYLES['title-line-1']}>World War I</span>
                    <span className={STYLES['title-line-2']}>Timeline</span>
                  </h1>
                </div>
              </div>
              <div className={STYLES.events}>
                <div className={STYLES.line}>
                  <TimelineEvents
                    militaryYears={militaryYears}
                    postServiceYears={postServiceYears}
                  />
                </div>
              </div>
            </div>
            <HowToCite id={tunnellerId} summary={data.summary} today={today} timeline />
          </>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
