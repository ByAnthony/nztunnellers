import { Articles } from '../../../types/article';

import STYLES from './HistoryChapters.module.scss';

type Props = {
    articles: Articles[]
  }

export function HistoryChapters({ articles }: Props) {
  return (
    <div className={STYLES['history-chapter']}>
      <div className={STYLES['chapter-cards-wrapper']}>
        <h2 id="history">
          History of their Company
        </h2>
        <div className={STYLES['chapter-cards']}>
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
