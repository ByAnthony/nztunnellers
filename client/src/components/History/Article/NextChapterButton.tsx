import { Next } from '../../../types/article';
import STYLES from '../History.module.scss';

type Props = {
    next: Next | null;
};

export function NextChapterButton({ next }: Props) {
  if (next) {
    return (
      <div className={STYLES['button-chapter-container']}>
        <a
          href={`/history/${next.url}`}
          className={STYLES['button-chapter']}
          aria-label={`Go to Chapter ${next.chapter}: ${next.title}`}
        >
          <div>
            <p>{`Chapter ${next.chapter}`}</p>
            <span>{next.title}</span>
          </div>
          <div className={STYLES.arrow}>&rarr;</div>
        </a>
      </div>
    );
  }
  return null;
}
