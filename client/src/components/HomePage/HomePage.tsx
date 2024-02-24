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
              The New Zealanders who fought underground
            </h1>
            <div className={STYLES['data-company']}>
              <p>
                one
                <span> company</span>
              </p>
              <p>
                seven
                <span> reinforcements</span>
              </p>
              <div className={STYLES['important-dates']}>
                <svg width="300" height="300">
                  <text>
                    <textPath xlinkHref="#circlePath" className={STYLES.established}>
                      Established in &bull; Established in &bull;
                      Established in &bull; Established in &bull;
                    </textPath>
                  </text>
                  <path id="circlePath" d="M 150, 150 m -100, 0 a 100,100 0 1,0 200,0 a 100,100 0 1,0 -200,0" fill="none" />
                  <text x="150" y="150" textAnchor="middle" alignmentBaseline="middle" className={STYLES['inside-circle-text']}>1915</text>
                </svg>
                <svg width="300" height="300" className={STYLES['disbanded-circle-container']}>
                  <path id="backgroundCircle" d="M 150, 150 m -115, 0 a 110,110 0 1,0 220,0 a 110,110 0 1,0 -220,0" fill="#181A1B" />
                  <text>
                    <textPath xlinkHref="#circlePath" className={STYLES.disbanded}>
                      Disbanded in &bull; Disbanded in &bull;
                      Disbanded in &bull; Disbanded in &bull;
                    </textPath>
                  </text>
                  <path id="circlePath" d="M 150, 150 m -100, 0 a 100,100 0 1,0 200,0 a 100,100 0 1,0 -200,0" fill="none" />
                  <text x="150" y="150" textAnchor="middle" alignmentBaseline="middle" className={STYLES['inside-circle-text']}>1919</text>
                </svg>
              </div>
            </div>
            <HistoryChapters articles={data} />
            <div className={STYLES['data-tunnellers']}>
              <p>936 men recruited in New Zealand</p>
              <p>average age: 32</p>
              <p>youngest: 16</p>
              <p>oldest: 58</p>
            </div>
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
