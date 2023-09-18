import { useGetAllHistoryArticleLinkQuery } from '../../redux/slices/historySlice';
import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';

import STYLES from './HomePage.module.scss';

export function HomePage() {
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
        <div className={STYLES.main}>
          <div className={STYLES.header}>
            <div className={STYLES['main-title']}>
              <h1>
                <span className={STYLES['title-line-1']}>The New Zealand</span>
                <span className={STYLES['title-line-2']}>Tunnelling Company</span>
              </h1>
            </div>
            <p className={STYLES['title-line-3']}>1915-1919</p>
          </div>
          <div className={STYLES.header} id="history">
            <div className={STYLES['main-title']}>
              <h1>
                <span className={STYLES['title-line-1']}>The Company</span>
                <span className={STYLES['title-line-2']}>History</span>
              </h1>
            </div>
          </div>
          <div className={STYLES.links}>
            {data.map((chapter) => (
              <div className={STYLES['link-container']} key={data.indexOf(chapter)}>
                <a
                  href={`/history/${chapter.url}`}
                  className={STYLES['link-button']}
                  aria-label={`Go to Chapter ${chapter.chapter}: ${chapter.title.replace('\\', ' ')}`}
                >
                  <div>
                    <p>{`Chapter ${chapter.chapter}`}</p>
                    <span>{chapter.title.replace('\\', ' ')}</span>
                  </div>
                  <div className={STYLES.arrow}>&rarr;</div>
                </a>
              </div>
            ))}
          </div>
        </div>
        )}
        <Footer />
      </div>
    );
  }
  return null;
}
