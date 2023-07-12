import { useGetAllHistoryArticleLinkQuery } from '../../redux/slices/rollSlice';
import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';
import STYLES from './History.module.scss';
import STYLES_TITLE from '../Roll/Roll.module.scss';

export function History() {
  const {
    data, error, isLoading, isSuccess,
  } = useGetAllHistoryArticleLinkQuery();

  if (data) {
    return (
      <>
        {error && (
          <div>
            <p>An error occured</p>
          </div>
        )}
        <Menu />
        { isLoading }
        { isSuccess && (
        <div className={STYLES_TITLE.container}>
          <h1>
            <span className={STYLES_TITLE['sub-title']}>The Company</span>
            <span className={STYLES_TITLE.title}>History</span>
          </h1>
          <div className={STYLES.links}>
            {data.map((chapter) => (
              <div className={STYLES['link-container']}>
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
      </>
    );
  }
  return null;
}
