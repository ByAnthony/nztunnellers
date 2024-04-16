import { Image, Section } from '../../../types/article';

import { Paragraph } from '../Paragraph/Paragraph';

import STYLES from './Content.module.scss';

type Props = {
    imageList: Image[] | undefined;
    sectionList: Section[];
};

export function Content({ imageList, sectionList }: Props) {
  if (imageList) {
    return (
      <>
        {sectionList.map((text, index) => (
          <div key={sectionList.indexOf(text)}>
            <Paragraph section={text} />
            {imageList.length > 0 && index < imageList.length ? (
              <>
                <div className={STYLES['image-container']}>
                  <img
                    className={STYLES.image}
                    src={`/images/history/${imageList[index].file}`}
                    alt={imageList[index].alt}
                  />
                </div>
                <div className={STYLES['image-legend']}>
                  <div className={STYLES.title}>{imageList[index].title}</div>
                  <div className={STYLES.captions}>{imageList[index].photographer}</div>
                  <div className={STYLES.reference}>{imageList[index].reference}</div>
                </div>
              </>
            ) : <br /> }
          </div>
        ))}
      </>
    );
  }
  return null;
}
