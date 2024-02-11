import { Footer } from '../Footer/Footer';
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
          <div className={STYLES['homepage-container']}>
            <h2 id="history">History of the Company</h2>
            <div className={STYLES['chapter-cards-wrapper']}>
              <div className={STYLES['chapter-cards']}>
                {data.map((article) => {
                  const divStyle = {
                    backgroundImage: `url(../images/history/${article.image})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center center',
                  };
                  return (
                    <a
                      href={`/history/${article.url}`}
                      className={STYLES['link-button']}
                      aria-label={`Go to Chapter ${article.chapter}: ${article.title.replace('\\', ' ')}`}
                    >
                      <div className={STYLES['chapter-card']} key={data.indexOf(article)} style={divStyle}>
                        <div className={STYLES['chapter-card-dimmer']}>
                          <div className={STYLES['chapter-card-content']}>
                            <div>
                              <p>{article.title.replace('\\', ' ')}</p>
                              <span>{`Chapter ${article.chapter}`}</span>
                            </div>
                          </div>
                        </div>
                      </div>
                    </a>
                  );
                })}
              </div>
            </div>
          </div>
        )}
        <Footer />
      </div>
    );
  }
  return null;
}
