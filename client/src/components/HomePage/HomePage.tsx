import { useGetHomepageDataQuery } from '../../redux/slices/homepageSlice';

import { Footer } from '../Footer/Footer';
import { HistoryChapters } from './HistoryChapters/HistoryChapter';
import { Menu } from '../Menu/Menu';
import { TunnellersImages } from './TunnellersImages/TunnellersImages';

import STYLES from './HomePage.module.scss';

export function HomePage() {
  const {
    data, error, isLoading, isSuccess,
  } = useGetHomepageDataQuery();

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
            <TunnellersImages images={data.tunnellers} />
            <div className={STYLES.intro}>
              <h1>
                The Kiwis who
                <br />
                fought underground
                <br />
                during World War I
              </h1>
            </div>
            <HistoryChapters articles={data.historyChapters} />
          </div>
        )}
        <Footer />
      </div>
    );
  }
  return null;
}
