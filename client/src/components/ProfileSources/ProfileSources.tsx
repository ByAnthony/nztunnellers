import type { NominalRoll, Sources } from '../../types/tunneller';
import STYLES from './ProfileSources.module.scss';

type Props = {
    sources: Sources,
}

export function ProfileSources({ sources }: Props) {
  const getNominalRoll = (nominalRoll: NominalRoll) => {
    if (nominalRoll.volume && nominalRoll.roll) {
      return (
        <p>
          <em>{ nominalRoll.title}</em>
          ,
          {' '}
          { nominalRoll.volume}
          ,
          {' '}
          { nominalRoll.roll }
          ,
          {' '}
          { nominalRoll.publisher}
          ,
          {' '}
          { nominalRoll.town}
          ,
          {' '}
          { nominalRoll.date}
          ,
          {' '}
          { nominalRoll.page }
          .
        </p>
      );
    }
    return (
      <p>
        <em>{ nominalRoll.title}</em>
        ,
        {' '}
        { nominalRoll.publisher}
        ,
        {' '}
        { nominalRoll.town}
        ,
        {' '}
        { nominalRoll.date}
        ,
        {' '}
        { nominalRoll.page }
        .
      </p>
    );
  };

  return (
    <div className={STYLES.sources}>
      <h3>Sources</h3>
      <ul>
        <li>
          <p>
            Auckland War Memorial Museum Tāmaki Paenga Hira:
            {' '}
            <a href={sources.awmmCenotaph} target="_blank" rel="noreferrer">Online Cenotaph He Toa Taumata Rau</a>
            .
          </p>
        </li>
        <li>
          { getNominalRoll(sources.nominalRoll) }
        </li>
      </ul>
    </div>
  );
}
