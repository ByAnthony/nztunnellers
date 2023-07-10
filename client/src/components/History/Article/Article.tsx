import { useParams } from 'react-router-dom';
import { useGetHistoryArticleByIdQuery } from '../../../redux/slices/rollSlice';
import { today } from '../../../utils/date-utils';
import { Footer } from '../../Footer/Footer';
import { Menu } from '../../Menu/Menu';
import STYLES from '../History.module.scss';

export function Article() {
  const { id } = useParams();
  const {
    data, error, isLoading, isSuccess,
  } = useGetHistoryArticleByIdQuery(id!);

  const formatText = (text: string) => {
    const paragraphs = text.split('\\n\\n');
    return paragraphs.map((paragraph) => (
      <p key={paragraphs.indexOf(paragraph)}>
        {paragraph
          .replace(/--/g, '\u00A0')
          .split(/(\*.+?\*)|(\[.+?\))/g)
          .map((segment) => {
            if (segment && segment.startsWith('*') && segment.endsWith('*')) {
              const italicText = segment.slice(1, -1);
              return <em key={paragraph.indexOf(segment)}>{italicText}</em>;
            }
            if (segment && segment.startsWith('[') && segment.endsWith(')')) {
              const linkText = segment.slice(1, -1);
              const [label, url] = linkText.split('](');
              if (url.includes('footnote')) {
                return (
                  <a key={paragraph.indexOf(segment)} href={url} id={`reference_${label}`}>
                    [
                    {label}
                    ]
                  </a>
                );
              }
              const number = label.slice(0, -1);
              return (
                <a key={paragraph.indexOf(segment)} href={url} id={`footnote_${number}`}>
                  {label}
                </a>
              );
            }
            return <span key={paragraph.indexOf(segment)}>{segment}</span>;
          })}
      </p>
    ));
  };

  if (data) {
    const [subTitle, title] = data.title.split('\\');
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
          <div className={STYLES['chapter-title']}>
            <h1>
              <span className={STYLES['sub-title']}>{subTitle}</span>
              <span className={STYLES.title}>{title}</span>
            </h1>
            <div className={STYLES['chapter-number']}>{data.chapter}</div>
          </div>
          <div className={STYLES['image-container']}>
            <img
              className={STYLES.image}
              src={`/images/history/${data.image[0].file}`}
              alt={data.image[0].alt}
            />
          </div>
          <div className={STYLES.article}>
            <div className={STYLES.paragraph}>
              <h2>{data.section[0].title}</h2>
              {formatText(data.section[0].text)}
            </div>
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
            <div className={STYLES.paragraph}>
              <h2>{data.section[1].title}</h2>
              {formatText(data.section[1].text)}
            </div>
          </div>
          <div className={STYLES['button-chapter-container']}>
            <a href={`/history/${data.next.url}`} className={STYLES['button-chapter']} aria-label={`Go to Chapter ${data.next.chapter}: ${data.next.title}`}>
              <div>
                <p>{`Chapter ${data.next.chapter}`}</p>
                <span>{data.next.title}</span>
              </div>
              <div className={STYLES.arrow}>&rarr;</div>
            </a>
          </div>
          <div className={STYLES.notes}>
            <h3>Notes</h3>
            {formatText(data.notes)}
          </div>
          <div className={STYLES.notes}>
            <h3>How to cite this page</h3>
            <p>
              Anthony Byledbal, &ldquo;
              {data.title.replace('\\', ' ')}
              &rdquo;,
              {' '}
              <em>New Zealand Tunnellers Website</em>
              ,
              {' '}
              {`${today.getFullYear()}`}
              {' '}
              (2009),
              Accessed:
              {' '}
              {`${today.toLocaleDateString('en-NZ', {
                year: 'numeric',
                month: 'long',
                day: 'numeric',
              })}. `}
            </p>
          </div>
        </div>
        )}
        <Footer />
      </>
    );
  }
  return null;
}
