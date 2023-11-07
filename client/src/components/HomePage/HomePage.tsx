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
                </a>
              </div>
            ))}
        </div>
        )}
        <Footer />
      </div>
    );
  }
  return null;
}
