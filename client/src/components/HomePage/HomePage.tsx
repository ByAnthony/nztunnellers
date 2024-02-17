import { Footer } from '../Footer/Footer';
import { useGetAllHistoryArticleLinkQuery } from '../../redux/slices/historySlice';
import { Menu } from '../Menu/Menu';

import STYLES from './HomePage.module.scss';
import { HistoryChapters } from './HistoryChapters/HistoryChapter';

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
            <h1>
              <span>The </span>
              Kiwis
              <span> who </span>
              fought underground
              <span> during World War I</span>
            </h1>
            <HistoryChapters articles={data} />
            <div className={STYLES['tunnellers-story']}>
              <h2>
                <span>
                  Stories
                  <span>of the</span>
                </span>
                Tunnellers
              </h2>
            </div>
          </div>
        )}
        <Footer />
      </div>
    );
  }
  return null;
}
