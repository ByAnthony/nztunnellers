import { useParams } from 'react-router-dom';
import { EventDetails, Events } from '../../types/tunneller';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import STYLES from './Timeline.module.scss';
import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';

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

    const disease = data.militaryYears.endOfService.deathWar?.cause?.circumstances;
    const warInjuries = data.postServiceYears.death?.cause?.circumstances;

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
            if (title && title === 'Enlisted') {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['main-event']}>
                  <p>{title}</p>
                  <span>{eventDetails.description}</span>
                </div>
              );
            }
            if (title && (title === 'Killed in action' || title === 'Died of wounds' || title === 'Died of disease' || title === 'Died of accident')) {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['main-event']}>
                  <span>{title}</span>
                  {title === 'Died of disease' && (disease && place())
                    ? (
                      <>
                        <span className={STYLES.info}>{` (${disease})`}</span>
                        <span className={STYLES['info-block']}>{place()}</span>
                      </>

                    )
                    : null}
                  {title === 'Died of disease' && (disease && !place())
                    ? (
                      <span className={STYLES.info}>{` (${disease})`}</span>

                    )
                    : null}
                  {title === 'Died of disease' && warInjuries
                    ? (
                      <span className={STYLES['info-block']}>{warInjuries}</span>
                    )
                    : null}
                  {title === 'Killed in action' && (eventDetails.description && place())
                    ? (
                      <>
                        <p className={STYLES['line-margin']}>{eventDetails.description}</p>
                        <span className={STYLES['info-block-with-description']}>{place()}</span>
                      </>
                    )
                    : null}
                  {title === 'Killed in action' && (!eventDetails.description && place())
                    ? (
                      <span className={STYLES['info-block']}>{place()}</span>
                    )
                    : null}
                  {title === 'Killed in action' && (eventDetails.description && !place())
                    ? (
                      <p>{eventDetails.description}</p>
                    )
                    : null}
                  {title === 'Died of wounds'
                    ? (
                      <span className={STYLES['info-block']}>{place()}</span>
                    )
                    : null}
                </div>
              );
            }
            if (title && (title === 'Buried' || title === 'Grave reference')) {
              return (
                <div key={event.event.indexOf(eventDetails)} className={STYLES['tunneller-event-with-title']}>
                  <p>{title}</p>
                  <span>{eventDetails.description}</span>
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
        <Menu />
        { isSuccess && (
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
