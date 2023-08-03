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
          <div className={STYLES['main-title']}>
            <h1>
              <span className={STYLES['title-line-1']}>The Company</span>
              <span className={STYLES['title-line-2']}>History</span>
            </h1>
          </div>
          <div className={STYLES.links}>
            {data.map((chapter) => {
              const [titleLine1, titleLine2] = chapter.title.split('\\');

              return (
                <div className={STYLES['link-container']}>
                  <a
                    href={`/history/${chapter.url}`}
                    className={STYLES['link-button']}
                    aria-label={`Go to Chapter ${chapter.chapter}: ${chapter.title.replace('\\', ' ')}`}
                  >
                    <div>
                      <p>{`Chapter ${chapter.chapter}`}</p>
                    </div>
                    <div>
                      <span className={STYLES['title-line-1']}>{titleLine1}</span>
                      <span className={STYLES['title-line-2']}>{titleLine2}</span>
                    </div>
                  </a>
                </div>
              );
            })}
          </div>
        </div>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
