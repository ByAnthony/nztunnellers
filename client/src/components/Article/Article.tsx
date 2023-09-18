import { useParams } from 'react-router-dom';
import { useGetHistoryArticleByIdQuery } from '../../redux/slices/rollSlice';

// import { invariant } from '../../utils/invariant';
import { today } from '../../utils/date';

import { Content } from './Content/Content';
import { Footer } from '../Footer/Footer';
import { HowToCite } from '../HowToCite/HowToCite';
import { Menu } from '../Menu/Menu';
import { NextChapterButton } from './NextChapterButton/NextChapterButton';
import { Notes } from './Notes/Notes';
import { Title } from '../Title/Title';
import { TopImage } from './TopImage/TopImage';

import STYLES from './Article.module.scss';

export function Article() {
  const { id = '' } = useParams();

  const {
    data, error, isLoading, isSuccess,
  } = useGetHistoryArticleByIdQuery(id);

  if (data) {
    return (
      <>
        {error && (
        <div className={STYLES.profile}>
          <p>An error occured</p>
        </div>
        )}
        <Menu />
        { isLoading }
        { isSuccess && (
        <div className={STYLES.container}>
          <div className={STYLES.header}>
            <div className={STYLES.link}>
              <a href="/#history">History</a>
            </div>
            <Title title={data.title} subTitle={data.chapter} />
          </div>
          <TopImage image={data.image[0]} />
          <Content imageList={data.image.slice(1)} sectionList={data.section} />
          <NextChapterButton chapter={data.next} />
          <Notes notes={data.notes} />
          <HowToCite title={data.title} today={today} />
        </div>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
