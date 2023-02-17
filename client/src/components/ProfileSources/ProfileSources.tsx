import type { Sources } from '../../types/tunneller';
import STYLES from './ProfileSources.module.scss';

type Props = {
    sources: Sources,
}

export function ProfileSources({ sources }: Props) {
  return (
    <div className={STYLES.sources}>
      <h2>Sources</h2>
      <ul>
        <li>
          <p>
            Auckland War Memorial Museum Tāmaki Paenga Hira:
            {' '}
            <a href={sources.awmmCenotaph} target="_blank" rel="noreferrer">Online Cenotaph He Toa Taumata Rau</a>
          </p>
        </li>
      </ul>
    </div>
  );
}
