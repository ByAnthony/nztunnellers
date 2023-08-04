import { useParams } from 'react-router-dom';
import { Footer } from '../../Footer/Footer';
import { Menu } from '../../Menu/Menu';
import { Title } from './Title/Title';
import { today } from '../../../utils/date-utils';
import { useGetHistoryArticleByIdQuery } from '../../../redux/slices/rollSlice';
import STYLES from './Article.module.scss';
import { HowToCite } from './HowToCite/HowToCite';
import { Notes } from './Notes/Notes';
import { NextChapterButton } from './NextChapterButton/NextChapterButton';
import { TopImage } from './TopImage/TopImage';
import { Content } from './Content/Content';

export function Article() {
  const { id } = useParams();
  const {
    data, error, isLoading, isSuccess,
  } = useGetHistoryArticleByIdQuery(id!);

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
            <Title title={data.title} chapter={data.chapter} />
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
