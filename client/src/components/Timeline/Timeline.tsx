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

    const place = () => {
      const location = data.militaryYears.endOfService.deathWar?.place?.location;
      const town = data.militaryYears.endOfService.deathWar?.place?.town;
      if (location && town) {
        return `${location}, ${town}`;
      }
      if (location && !town) {
        return location;
      }
      return null;
    };

    const circumstances = data.militaryYears.endOfService.deathWar?.cause?.circumstances;

    const timeline = frontEvents.map((event: Events) => (
      <div key={frontEvents.indexOf(event)}>
        <div className={STYLES.date}>
          <div className={STYLES.year}>{`${event.date.year}`}</div>
          <div className={STYLES['day-month']}>{`${event.date.dayMonth}`}</div>
        </div>
        <div className={STYLES['event-wrapper']}>
          {event.event.map((eventDetails: EventDetails) => {
            const { title } = eventDetails;
            if (title && title === 'The Company') {
              return (
                <div key={event.event.indexOf(eventDetails)}>
                  <div className={STYLES['company-event']}>
                    <img src={`/images/roll/${eventDetails.image}`} alt="" />
                    <p>{eventDetails.description}</p>
                  </div>
                </div>
              );
            }
            if (title && (title === 'Trained' || title === 'Posted')) {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['tunneller-event-with-title']}>
                  <p>{title}</p>
                  <span>{eventDetails.description}</span>
                </div>
              );
            }
            if (title && (title === 'Enlisted' || title === 'Killed in action' || title === 'Died of wounds' || title === 'Died of disease' || title === 'Died of accident')) {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['main-event']}>
                  <span>{title}</span>
                  {title === 'Killed in action' || title === 'Died of wounds'
                    ? (
                      <span className={STYLES.place}>{place()}</span>
                    )
                    : null}
                  {title === 'Died of disease' && circumstances
                    ? (
                      <span className={STYLES.circumstances}>{` (${circumstances})`}</span>
                    )
                    : null}
                  {eventDetails.description ? <p>{eventDetails.description}</p> : null}
                </div>
              );
            }
            if (title && (title === 'Buried' || title === 'Grave reference')) {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['tunneller-event-with-title']}>
                  <span>{title}</span>
                  <p>{eventDetails.description}</p>
                </div>
              );
            }
            if (!title) {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['tunneller-event']}>
                  <p>{eventDetails.description}</p>
                </div>
              );
            }
            return (
              <div key={event.event.indexOf(eventDetails)} className={STYLES['main-event']}>
                <p>{title}</p>
                <span>{eventDetails.description}</span>
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
          <Link to={`/roll/${tunnellerId}`} key={tunnellerId} aria-label={`Back to ${name.forename} ${name.surname} profile.`}>
            <div className={STYLES.back}>
              <div className={STYLES['arrow-left']}>&larr;</div>
              <div className={STYLES.profile}>{`${name.forename} ${name.surname}`}</div>
            </div>
          </Link>
          <h1>Timeline</h1>
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
