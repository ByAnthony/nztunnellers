import { useEffect } from 'react';
import { useGetAllHistoryArticleLinkQuery } from '../../redux/slices/historySlice';
import { Menu } from '../Menu/Menu';

import STYLES from './HomePage.module.scss';

export function HomePage() {
  useEffect(() => {
    window.addEventListener('scroll', () => {
      const scrollPosition = window.scrollY;
      const translateValue = `translateX(${-scrollPosition}px)`;
      document.getElementById('chapterCards')!.style.transform = translateValue;
    });
  });

  const {
    data, error, isLoading, isSuccess,
  } = useGetAllHistoryArticleLinkQuery();

  if (data) {
    return (
      <div className={STYLES.homepage}>
        {error && (
        <div>
          <p>An error occured</p>
        </div>
        )}
        <Menu />
        { isLoading }
        { isSuccess && (
          <div className={STYLES['homepage-container']}>
            <h2>History of the Company</h2>
            <div className={STYLES['chapter-cards']} id="chapterCards">
              {data.map((article) => {
                const divStyle = {
                  backgroundImage: `url(../images/history/${article.image})`,
                  backgroundSize: 'cover',
                };

                return (
                  <div className={STYLES['chapter-card']} key={data.indexOf(article)} style={divStyle}>
                    <a
                      href={`/history/${article.url}`}
                      className={STYLES['link-button']}
                      aria-label={`Go to Chapter ${article.chapter}: ${article.title.replace('\\', ' ')}`}
                    >
                      <div>
                        <p>{article.chapter}</p>
                        <span>{article.title.replace('\\', ' ')}</span>
                      </div>
                    </a>
                  </div>
                );
              })}
            </div>
          </div>
        )}
        {/* <Footer /> */}
      </div>
    );
  }
  return null;
}
