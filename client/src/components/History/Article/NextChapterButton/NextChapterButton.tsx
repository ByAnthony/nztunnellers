import { Next } from '../../../../types/article';
import STYLES from './NextChapterButton.module.scss';

type Props = {
    chapter: Next | undefined;
};

export function NextChapterButton({ chapter }: Props) {
  if (chapter) {
    return (
      <div className={STYLES['button-chapter-container']}>
        <a
          href={`/history/${chapter.url}`}
          className={STYLES['button-chapter']}
          aria-label={`Go to Chapter ${chapter.chapter}: ${chapter.title.replace('\\', ' ')}`}
        >
          <div>
            <p className={STYLES.chapter}>{`Chapter ${chapter.chapter}`}</p>
            <span>{chapter.title.replace('\\', ' ')}</span>
          </div>
          <div className={STYLES.arrow}>&rarr;</div>
        </a>
      </div>
    );
  }
  return null;
}
