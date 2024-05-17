import { useRef } from 'react';
import { Articles } from '../../../types/article';

import STYLES from './HistoryChapters.module.scss';

type Props = {
    articles: Articles[]
  }

export function HistoryChapters({ articles }: Props) {
  const containerRef = useRef<HTMLDivElement>(null);

  const scrollLeft = () => {
    if (containerRef.current) {
      const scrollAmount = 301;
      containerRef.current.scrollLeft -= scrollAmount;
    }
  };

  const scrollRight = () => {
    if (containerRef.current) {
      const scrollAmount = 301;
      containerRef.current.scrollLeft += scrollAmount;
    }
  };

  return (
    <div className={STYLES['history-chapter']}>
      <div id="history" className={STYLES['chapter-cards-wrapper']}>
        <div className={STYLES['chapter-cards-menu']}>
          <h3>
            History of the Company
          </h3>
          <div className={STYLES['chapter-cards-nav']}>
            <button type="button" onClick={scrollLeft} aria-label="Scroll to the left to see next chapters">&larr;</button>
            <button type="button" onClick={scrollRight} aria-label="Scroll to the right to see previous chapters">&rarr;</button>
          </div>
        </div>
        <div className={STYLES['chapter-cards']} ref={containerRef}>
          {articles.map((article) => {
            const divStyle = {
              backgroundImage: `url(../images/history/${article.image})`,
              backgroundSize: 'cover',
              backgroundPosition: 'center center',
            };
            const splitTitle = (string: string) => {
              const split = string.split('\\');
              return split;
            };
            return (
              <div className={STYLES['chapter-card']} key={articles.indexOf(article)} style={divStyle}>
                <a
                  href={`/history/${article.url}`}
                  className={STYLES['link-button']}
                  aria-label={`Go to Chapter ${article.chapter}: ${article.title.replace(/\\/g, ' ')}`}
                >
                  <div className={STYLES['chapter-card-dimmer']}>
                    <div className={STYLES['chapter-card-content']}>
                      <div>
                        <span className={STYLES['title-line-1']}>{ splitTitle(article.title)[0] }</span>
                        <span className={STYLES['title-line-2']}>{ splitTitle(article.title)[1] }</span>
                        <span className={STYLES['title-line-3']}>{`Chapter ${article.chapter}`}</span>
                      </div>
                    </div>
                  </div>
                </a>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
