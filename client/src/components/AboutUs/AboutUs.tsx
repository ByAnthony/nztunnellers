import { Content } from '../Article/Content/Content';
import { Footer } from '../Footer/Footer';
import { Menu } from '../Menu/Menu';
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
          <div className={STYLES['image-container']}>
            <img
              className={STYLES.image}
              src={`/images/about-us/${data.image[0].file}`}
              alt={data.image[0].alt}
            />
          </div>
          <Content imageList={data.image.slice(1)} sectionList={data.section} />
        </div>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
