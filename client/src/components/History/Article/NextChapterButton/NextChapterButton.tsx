import { Next } from '../../../../types/article';
import STYLES from './NextChapterButton.module.scss';

type Props = {
    next: Next | undefined;
};

export function NextChapterButton({ next }: Props) {
  if (next) {
    return (
      <div className={STYLES['button-chapter-container']}>
        <a
          href={`/history/${next.url}`}
          className={STYLES['button-chapter']}
          aria-label={`Go to Chapter ${next.chapter}: ${next.title.replace('\\', ' ')}`}
        >
          <div>
            <p>{`Chapter ${next.chapter}`}</p>
            <span>{next.title.replace('\\', ' ')}</span>
          </div>
          <div className={STYLES.arrow}>&rarr;</div>
        </a>
      </div>
    );
  }
  return null;
}
