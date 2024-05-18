import { useRef, useState } from 'react';
import { Articles } from '../../../types/article';

import STYLES from './HistoryChapters.module.scss';

type Props = {
    articles: Articles[]
  }

export function HistoryChapters({ articles }: Props) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);

  const scrollLeft = () => {
    if (containerRef.current) {
      const container = containerRef.current;
      container.scrollTo({
        left: container.scrollLeft - (container.clientWidth / 3),
      });
      setCurrentIndex((prevIndex) => Math.min(prevIndex - 1));
    }
  };

  const scrollRight = () => {
    if (containerRef.current) {
      const container = containerRef.current;
      container.scrollTo({
        left: container.scrollLeft + (container.clientWidth / 3),
      });
      setCurrentIndex((prevIndex) => Math.min(prevIndex + 1));
    }
  };

  const isLastCard = currentIndex === articles.length - 3;
  const isFirstCard = currentIndex === 0;

  const buttonDisabledStyle = { color: 'rgb(44, 46, 47)', cursor: 'not-allowed' };
  const buttonFirstCard = isFirstCard ? buttonDisabledStyle : {};
  const buttonLastCard = isLastCard ? buttonDisabledStyle : {};

  return (
    <div className={STYLES['history-chapter']}>
      <div id="history" className={STYLES['chapter-cards-wrapper']}>
        <div className={STYLES['chapter-cards-menu']}>
          <h3>
            History of the Company
          </h3>
          <div className={STYLES['chapter-cards-nav']}>
            <button type="button" onClick={scrollLeft} disabled={isFirstCard} style={buttonFirstCard} aria-label="Scroll to the left to see previous chapters">&larr;</button>
            <button type="button" onClick={scrollRight} disabled={isLastCard} style={buttonLastCard} aria-label="Scroll to the right to see next chapters">&rarr;</button>
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
