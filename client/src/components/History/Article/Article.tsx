import { useParams } from 'react-router-dom';
import { Footer } from '../../Footer/Footer';
import { Menu } from '../../Menu/Menu';
import { Title } from './Title';
import { today } from '../../../utils/date-utils';
import { useGetHistoryArticleByIdQuery } from '../../../redux/slices/rollSlice';
import STYLES from '../History.module.scss';
import { Paragraph } from './Paragraph';
import { HowToCite } from './HowToCite';
import { Notes } from './Notes';
import { NextChapterButton } from './NextChapterButton';

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
          <div className={STYLES.link}>
            <a href="/history">History</a>
            <span>/</span>
          </div>
          <Title title={data.title} chapter={data.chapter} />
          <div className={STYLES['image-container']}>
            <img
              className={STYLES.image}
              src={`/images/history/${data.image[0].file}`}
              alt={data.image[0].alt}
            />
          </div>
          <div className={STYLES.article}>
            <Paragraph section={data.section[0]} />
            <div className={STYLES['image-container']}>
              <img
                className={STYLES.image}
                src={`/images/history/${data.image[1].file}`}
                alt={data.image[1].alt}
              />
            </div>
            <div className={STYLES['image-legend']}>
              <div className={STYLES.title}>{data.image[1].title}</div>
              <div className={STYLES.captions}>{data.image[1].photographer}</div>
              <div className={STYLES.reference}>{data.image[1].reference}</div>
            </div>
            <Paragraph section={data.section[1]} />
          </div>
          <NextChapterButton next={data.next} />
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
