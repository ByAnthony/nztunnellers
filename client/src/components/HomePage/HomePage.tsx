import { useGetAllHistoryArticleLinkQuery } from '../../redux/slices/historySlice';

import { Footer } from '../Footer/Footer';
import { HistoryChapters } from './HistoryChapters/HistoryChapter';
import { Menu } from '../Menu/Menu';
import { Title } from '../Title/Title';

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
            <div className={STYLES.title}>
              <Title
                title={'The Kiwis\\Also Dig Tunnels'}
                subTitle="Fighting underground during World War I"
              />
            </div>
            <div className={STYLES.tunnellers}>
              <h2>
                The Tunnellers
              </h2>
              <div className={STYLES.enlistment}>
                <div className={STYLES['total-recruits']}>
                  <svg width="300" height="300">
                    <text>
                      <textPath xlinkHref="#circlePath" className={STYLES['circle-path']}>
                        Total number of men recruited &bull;
                        Total number of men recruited &bull;
                      </textPath>
                    </text>
                    <path id="circlePath" d="M 150, 150 m -100, 0 a 100,100 0 1,0 200,0 a 100,100 0 1,0 -200,0" fill="none" />
                    <text x="150" y="150" textAnchor="middle" alignmentBaseline="middle" className={STYLES['inside-circle-text']}>936</text>
                  </svg>
                </div>
                <div className={STYLES.age}>
                  <h3>Age at enlistment</h3>
                  <div className={STYLES['age-content-wrapper']}>
                    <div className={STYLES['age-content']}>
                      <div className={STYLES['age-card']} id={STYLES.oldest}>
                        <span>Oldest</span>
                        <p>58</p>
                      </div>
                      <div className={STYLES['age-card']} id={STYLES.average}>
                        <span>Average</span>
                        <p>32</p>
                      </div>
                      <div className={STYLES['age-card']} id={STYLES.youngest}>
                        <span>Youngest</span>
                        <p>16</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className={STYLES['marital-status']}>
                <h3>Marital status</h3>
                <div className={STYLES['marital-status-wrapper']}>
                  <div className={STYLES['marital-status-card']} id={STYLES.single}>
                    <span>Single</span>
                    <p>75%</p>
                  </div>
                  <div className={STYLES['marital-status-card']} id={STYLES.married}>
                    <p>25%</p>
                    <span>Married</span>
                  </div>
                </div>
              </div>
              <div className={STYLES.professions}>
                <h3>Professions</h3>
                <div className={STYLES['professions-content-wrapper']}>
                  <div className={STYLES['professions-title']}>
                    <p>Miners</p>
                  </div>
                  <div className={STYLES['professions-content']}>
                    <div>
                      <p className={STYLES.line}>1</p>
                      <div className={STYLES.ten}>2</div>
                    </div>
                    <div className={STYLES['circles-wrapper']}>
                      <div className={STYLES.circles}>
                        <div className={STYLES['plain-circle']} />
                        <div className={STYLES.circle} />
                        <div className={STYLES['plain-circle']} />
                        <div className={STYLES.circle} />
                        <div className={STYLES['plain-circle']} />
                      </div>
                      <div className={STYLES.circles}>
                        <div className={STYLES.circle} />
                        <div className={STYLES['plain-circle']} />
                        <div className={STYLES.circle} />
                        <div className={STYLES['plain-circle']} />
                        <div className={STYLES.circle} />
                      </div>
                    </div>
                  </div>
                </div>
                <div className={STYLES['marital-status-wrapper']}>
                  <div className={STYLES['marital-status-card']} id={STYLES['gold-miners']}>
                    <span>Gold mining</span>
                    <p>50%</p>
                  </div>
                  <div className={STYLES['marital-status-card']} id={STYLES['coal-miners']}>
                    <p>50%</p>
                    <span>Coal mining</span>
                  </div>
                </div>
                <div className={STYLES['marital-status-wrapper']}>
                  <div className={STYLES['marital-status-card']} id={STYLES['trade-union']}>
                    <span>Trade unionists</span>
                    <p>Most likely</p>
                  </div>
                </div>
              </div>
            </div>
            <div className={STYLES['image-container']}>
              <img
                className={STYLES.image}
                src="/images/homepage/arras.jpg"
                alt="Some tunnellers in Arras"
              />
            </div>

            <div className={STYLES.company}>
              <h2>The Company</h2>
              <p className={STYLES.introduction}>
                The New Zealand tunnellers were gathered in a single military company.
                Seven reinforcements followed which were originally planned every 6 months.
                The Main Body and the 1st Reinforcements left New Zealand on the same day,
                on the 18&nbsp;December 1915.
              </p>
              <div className={STYLES['company-content-wrapper']}>
                <div className={STYLES['company-content']}>
                  <div className={STYLES['company-card']} id={STYLES['main-body-background']}>
                    <div className={STYLES.contingent} id={STYLES['main-body']}>
                      <span>Main Body</span>
                      <p>423 recruits</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>18 December 1915</span>
                    </div>
                  </div>
                  <div className={STYLES['company-card']}>
                    <div className={STYLES.contingent} id={STYLES['reinforcements-1']}>
                      <span>1st Reinforcements</span>
                      <p>103</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>18 December 1915</span>
                    </div>
                  </div>
                  <div className={STYLES['company-card']}>
                    <div className={STYLES.contingent} id={STYLES['reinforcements-2']}>
                      <span>2nd Reinforcements</span>
                      <p>100</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>26 June 1916</span>
                    </div>
                  </div>
                  <div className={STYLES['company-card']}>
                    <div className={STYLES.contingent} id={STYLES['reinforcements-3']}>
                      <span>3rd Reinforcements</span>
                      <p>135</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>15 November 1916</span>
                    </div>
                  </div>
                  <div className={STYLES['company-card']}>
                    <div className={STYLES.contingent} id={STYLES['reinforcements-4']}>
                      <span>4th Reinforcements</span>
                      <p>77</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>16 February 1917</span>
                    </div>
                  </div>
                  <div className={STYLES['company-card']}>
                    <div className={STYLES.contingent} id={STYLES['reinforcements-5']}>
                      <span>5th Reinforcements</span>
                      <p>96</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>26 April 1917</span>
                    </div>
                  </div>
                  <div className={STYLES['company-card']}>
                    <div className={STYLES.contingent} id={STYLES['reinforcements-6']}>
                      <span>6th Reinforcements</span>
                      <p>51</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>26 July 1917</span>
                    </div>
                  </div>
                  <div className={STYLES['company-card']}>
                    <div className={STYLES.contingent} id={STYLES['reinforcements-7']}>
                      <span>7th Reinforcements</span>
                      <p>32</p>
                    </div>
                    <div className={STYLES.departure}>
                      <span>22 November 1917</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <HistoryChapters articles={data} />
          </div>
        )}
        <Footer />
      </div>
    );
  }
  return null;
}
