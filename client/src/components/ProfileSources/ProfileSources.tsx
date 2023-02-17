import type { NominalRoll, Sources } from '../../types/tunneller';
import STYLES from './ProfileSources.module.scss';

type Props = {
    sources: Sources,
}

export function ProfileSources({ sources }: Props) {
  const getNominalRoll = (nominalRoll: NominalRoll) => {
    if (nominalRoll.volume && nominalRoll.roll) {
      return `${nominalRoll.title}, ${nominalRoll.volume},
      ${nominalRoll.roll}, ${nominalRoll.publisher}, ${nominalRoll.town}, ${nominalRoll.date}, ${nominalRoll.page}.`;
    }
    return (
      `${nominalRoll.title}, ${nominalRoll.publisher}, ${nominalRoll.town}, ${nominalRoll.date}, ${nominalRoll.page}.`
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
          <p>{ getNominalRoll(sources.nominalRoll) }</p>
        </li>
      </ul>
    </div>
  );
}
