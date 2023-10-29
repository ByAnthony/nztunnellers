import { TimelineEvent } from '../TimelineEvent/TimelineEvent';
import {
  Event, MilitaryYears, PostServiceYears,
} from '../../../types/tunneller';

import STYLES from '../Timeline.module.scss';

type Props = {
    militaryYears: MilitaryYears,
    postServiceYears: PostServiceYears,
}

export function TimelineEvents({ militaryYears, postServiceYears }: Props) {
  const { frontEvents } = militaryYears;
  const frontEventsByYear = Object.entries(frontEvents);

  const place = () => {
    const location = militaryYears.endOfService.deathWar?.place?.location;
    const town = militaryYears.endOfService.deathWar?.place?.town;
    if (location && town) {
      return `${location}, ${town}`;
    }
    if (location && !town) {
      return location;
    }
    return null;
  };

  const disease = militaryYears.endOfService.deathWar?.cause?.circumstances;

  const warInjuries = postServiceYears.death?.cause?.circumstances;

  return (
    <>
      {frontEventsByYear.map(([key, events]) => (
        <div key={key}>
          <h2 className={STYLES['year-title']} key={key} aria-label={`Year ${key}`}>{key}</h2>
          {events.map((event: Event) => (
            <div key={events.indexOf(event)}>
              <div className={STYLES.date}>
                <div className={STYLES.year}>{`${event.date.year}`}</div>
                <div className={STYLES['day-month']}>{`${event.date.dayMonth}`}</div>
              </div>
              <div className={STYLES['event-wrapper']}>
                <TimelineEvent
                  event={event.event}
                  place={place}
                  disease={disease}
                  warInjuries={warInjuries}
                />
              </div>
            </div>
          ))}
        </div>
      ))}
    </>
  );
}
