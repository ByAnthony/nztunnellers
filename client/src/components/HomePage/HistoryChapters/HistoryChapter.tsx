import { useRef, useState } from 'react';
import { Articles } from '../../../types/article';

import STYLES from './HistoryChapters.module.scss';

type Props = {
    articles: Articles[]
  }

export function HistoryChapters({ articles }: Props) {
  const [currentIndex, setCurrentIndex] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);

  const scrollClick = (index: number) => {
    if (containerRef.current) {
      containerRef.current.scrollTo({
        left: index * (containerRef.current.clientWidth / 3),
      });
    }
  };

  const handleScrollLeft = () => {
    if (containerRef.current) {
      const previousIndex = currentIndex - 1;
      scrollClick(previousIndex);
      setCurrentIndex(previousIndex);
    }
  };

  const handleScrollRight = () => {
    if (containerRef.current) {
      const nextIndex = currentIndex + 1;
      scrollClick(nextIndex);
      setCurrentIndex(nextIndex);
    }
  };

  const handleScroll = () => {
    if (containerRef.current) {
      const { scrollLeft, clientWidth } = containerRef.current;
      const cardWidth = clientWidth / 3;
      const nextIndex = Math.round(scrollLeft / cardWidth);
      if (currentIndex !== nextIndex) {
        setCurrentIndex(nextIndex);
      }
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
            <button type="button" onClick={handleScrollLeft} disabled={isFirstCard} style={buttonFirstCard} aria-label="Scroll to the left to see previous chapters">&larr;</button>
            <button type="button" onClick={handleScrollRight} disabled={isLastCard} style={buttonLastCard} aria-label="Scroll to the right to see next chapters">&rarr;</button>
          </div>
        </div>
        <div className={STYLES['chapter-cards']} ref={containerRef} onScroll={handleScroll}>
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
