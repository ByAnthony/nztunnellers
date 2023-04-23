import { Link, useParams } from 'react-router-dom';
import { EventDetails, Events } from '../../types/tunneller';
import { useGetTunnellerByIdQuery } from '../../redux/slices/rollSlice';
import STYLES from './Timeline.module.scss';

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
        <div>{`${event.date.dayMonth} ${event.date.year}`}</div>
        <div>
          {event.event.map((eventDetails: EventDetails) => {
            const title = eventDetails.title ? <div>{`${eventDetails.title}`}</div> : null;
            return (
              <li key={event.event.indexOf(eventDetails)}>
                {title}
                <div>{`${eventDetails.description}`}</div>
                <p />
              </li>
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
            <div>&larr; Back</div>
          </Link>
          <p />
          <div>{`${name.forename} ${name.surname}`}</div>
          <div>{timeline}</div>
        </div>
        )}
      </>
    );
  }
  return null;
}
