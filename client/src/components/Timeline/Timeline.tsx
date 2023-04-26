import { Link, useParams } from 'react-router-dom';
import { EventDetails, Events } from '../../types/tunneller';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import STYLES from './Timeline.module.scss';
import { Footer } from '../Footer/Footer';

export function Timeline() {
  const { id } = useParams();
  const tunnellerId = Number(id);
  const {
    data, error, isLoading, isSuccess,
  } = useGetTunnellerByIdQuery(tunnellerId);

  if (data) {
    const { name } = data.summary;
    const { frontEvents } = data.militaryYears;

    const timeline = frontEvents.map((event: Events) => (
      <div key={frontEvents.indexOf(event)}>
        <div className={STYLES.date}>
          <div className={STYLES.year}>{`${event.date.year}`}</div>
          <div className={STYLES['day-month']}>{`${event.date.dayMonth}`}</div>
        </div>
        <div className={STYLES['event-wrapper']}>
          {event.event.map((eventDetails: EventDetails) => {
            const { title } = eventDetails;
            if (title && title !== 'The Company') {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['main-event']}>
                  <p>{title}</p>
                  <span>{eventDetails.description}</span>
                </div>
              );
            }
            if (title && title === 'The Company') {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['main-event']}>
                  <p>{eventDetails.description}</p>
                </div>
              );
            }
            return (
              <div key={event.event.indexOf(eventDetails)} className={STYLES.event}>
                <p>{eventDetails.description}</p>
              </div>
            );
          })}
        </div>
      </div>
    ));

    return (
      <>
        {error && (
        <div className={STYLES.timeline}>
          <p>An error occured</p>
        </div>
        )}
        { isLoading }
        { isSuccess && (
        <div className={STYLES.timeline}>
          <Link to={`/roll/${tunnellerId}`} className={STYLES.back} key={tunnellerId} aria-label={`Back to ${name.forename} ${name.surname} profile.`}>
            <div>&larr; Back</div>
          </Link>
          <h1>
            <span className={STYLES.forename}>World War I (1914-1918)</span>
            <span className={STYLES.surname}>New Zealand Tunnellers</span>
          </h1>
          <h2 className={STYLES.name}>{`${name.forename} ${name.surname}`}</h2>
          <div>
            <div className={STYLES.line}>
              {timeline}
            </div>
          </div>
        </div>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
