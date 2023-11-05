import { EventDetail } from '../../../types/tunneller';

import STYLES from '../Timeline.module.scss';

type Props = {
    event: EventDetail[],
    place: () => string | null,
    disease: string | undefined,
    warInjuries: string | undefined
}

export function TimelineEvent({
  event, place, disease, warInjuries,
}: Props) {
  return (
    <>
      {event.map((eventDetail: EventDetail) => {
        const { title } = eventDetail;

        if (eventDetail.title) {
          if (title === 'The Company') {
            return (
              <div key={event.indexOf(eventDetail)}>
                <div className={STYLES['company-event']}>
                  <img src={`/images/roll/${eventDetail.image}`} alt="" />
                  <p>{eventDetail.description}</p>
                </div>
              </div>
            );
          }

          if (title === 'Enlisted' || title === 'Posted') {
            return (
              <div key={event.indexOf(eventDetail)} className={STYLES['main-event']}>
                <p>{title}</p>
                <span>{eventDetail.description}</span>
              </div>
            );
          }

          if (title === 'Trained') {
            return (
              <div key={event.indexOf(eventDetail)} className={STYLES['tunneller-event-with-title']}>
                <p>{title}</p>
                <span>{eventDetail.description}</span>
              </div>
            );
          }

          if (title === 'Killed in action' || title === 'Died of wounds' || title === 'Died of disease' || title === 'Died of accident') {
            return (
              <div key={event.indexOf(eventDetail)} className={STYLES['main-event']}>
                <span>{title}</span>
                {title === 'Died of disease' && disease && place()
                  && (
                    <>
                      <span className={STYLES.info}>{` (${disease})`}</span>
                      <span className={STYLES['info-block']}>{place()}</span>
                    </>
                  )}
                {title === 'Died of disease' && disease && !place()
                  && (
                    <span className={STYLES.info}>{` (${disease})`}</span>
                  )}
                {title === 'Died of disease' && warInjuries
                  && (
                    <span className={STYLES['info-block']}>{warInjuries}</span>
                  )}
                {title === 'Killed in action' && eventDetail.description && place()
                  && (
                    <>
                      <p className={STYLES['line-margin']}>{eventDetail.description}</p>
                      <span className={STYLES['info-block-with-description']}>{place()}</span>
                    </>
                  )}
                {title === 'Killed in action' && !eventDetail.description && place()
                  && (
                    <span className={STYLES['info-block']}>{place()}</span>
                  )}
                {title === 'Killed in action' && eventDetail.description && !place()
                  && (
                    <p>{eventDetail.description}</p>
                  )}
                {title === 'Died of wounds'
                  && (
                    <span className={STYLES['info-block']}>{place()}</span>
                  )}
                {title === 'Died of accident'
                  && (
                    <span className={STYLES['info-block-with-description']}>{eventDetail.description}</span>
                  )}
              </div>
            );
          }

          if (title === 'Buried' || title === 'Grave reference') {
            return (
              <div key={event.indexOf(eventDetail)} className={STYLES['tunneller-event-with-title']}>
                <p>{title}</p>
                <span>{eventDetail.description}</span>
              </div>
            );
          }

          return (
            <div key={event.indexOf(eventDetail)} className={STYLES['main-event']}>
              <p>{title}</p>
              <span>{eventDetail.description}</span>
            </div>
          );
        }

        return (
          <div key={event.indexOf(eventDetail)} className={STYLES['tunneller-event']}>
            <p>{eventDetail.description}</p>
          </div>
        );
      })}
    </>
  );
}
