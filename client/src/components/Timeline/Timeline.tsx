import { useParams } from 'react-router-dom';
import { Title } from '../Title/Title';
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
                  <a href={`/tunnellers/${tunnellerId}`}>{`${data.summary.name.forename} ${data.summary.name.surname}`}</a>
                </div>
                <div className={STYLES['main-title']}>
                  <Title title={'World War I\\Timeline'} />
                </div>
              </div>
              <div className={STYLES.events}>
                <div className={STYLES.line}>
                  <TimelineEvents
                    militaryYears={data.militaryYears}
                    postServiceYears={data.postServiceYears}
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
