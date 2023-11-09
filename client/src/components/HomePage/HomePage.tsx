import { useGetAllHistoryArticleLinkQuery } from '../../redux/slices/historySlice';
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
            {data.map((article) => {
              const divStyle = {
                backgroundImage: `url(../images/history/${article.image.file})`,
                backgroundSize: 'cover',
              };

              return (
                <div className={STYLES['link-container']} key={data.indexOf(article)} style={divStyle}>
                  <div className={STYLES.test}>
                    <a
                      href={`/history/${article.url}`}
                      className={STYLES['link-button']}
                      aria-label={`Go to Chapter ${article.chapter}: ${article.title.replace('\\', ' ')}`}
                    >
                      <div>
                        <p>History of the Company</p>
                        <span>{article.title.replace('\\', ' ')}</span>
                        <p>{`Chapter ${article.chapter}`}</p>
                      </div>
                    </a>
                  </div>
                </div>
              );
            })}
        </div>
        )}
        {/* <Footer /> */}
      </div>
    );
  }
  return null;
}
