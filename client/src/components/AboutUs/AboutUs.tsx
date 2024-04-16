import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';
import { Paragraph } from '../Article/Paragraph/Paragraph';
import { Title } from '../Title/Title';

import STYLES from './AboutUs.module.scss';
import { useGetAboutUsQuery } from '../../redux/slices/aboutUsSlice';

export function AboutUs() {
  const {
    data, error, isLoading, isSuccess,
  } = useGetAboutUsQuery();

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
            <Title title={data.title} />
          </div>
          <Paragraph section={data.section[0]} />
          <div className={STYLES['image-container']}>
            <img
              className={STYLES.image}
              src={`/images/about-us/${data.image[0].file}`}
              alt={data.image[0].alt}
            />
          </div>
          <Paragraph section={data.section[1]} />
        </div>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
