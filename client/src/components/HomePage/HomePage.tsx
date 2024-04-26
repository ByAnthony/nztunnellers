import { useGetAllHistoryArticleLinkQuery } from '../../redux/slices/historySlice';

import { Footer } from '../Footer/Footer';
import { HistoryChapters } from './HistoryChapters/HistoryChapter';
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
            <HistoryChapters articles={data} />
          </div>
        )}
        <Footer />
      </div>
    );
  }
  return null;
}
