import { ImageSource, ImageBookAuthor } from '../../types/tunneller';
import STYLES from './ProfileImageSource.module.scss';

type props = {
    source: ImageSource | undefined,
}

export function ProfileImageSource({ source }: props) {
  const displayImageSource = (imageSource: ImageSource | undefined) => {
    const title = <h3>Photograph</h3>;
    if (imageSource?.archives) {
      return (
        <>
          {title}
          <p>{`${imageSource.archives.location}, ${imageSource.archives.reference}.`}</p>
        </>
      );
    }
    if (imageSource?.aucklandLibraries) {
      const displayReference = (url: string) => url.slice(url.indexOf('=') + 1, url.indexOf('&'));
      return (
        <>
          {title}
          <p>
            Auckland Libraries Ngā Pātaka Kōrero o Tāmaki Makaurau,
            Sir George Grey Special Collections:
            {' '}
            <a href={`${imageSource.aucklandLibraries}`}>{displayReference(imageSource.aucklandLibraries)}</a>
            .
          </p>
        </>
      );
    }
    if (imageSource?.family) {
      return (
        <>
          {title}
          <p>{`Courtesy of ${imageSource?.family}.`}</p>
        </>
      );
    }
    if (imageSource?.newspaper) {
      return (
        <>
          {title}
          <p>
            <em>{imageSource?.newspaper.name}</em>
            {`, ${imageSource?.newspaper.date}.`}
          </p>
        </>
      );
    }
    if (imageSource?.book) {
      const displayAuthors = (authors: ImageBookAuthor[]) => {
        if (authors.length === 2) {
          return `${authors[0].forename} ${authors[0].surname} and ${authors[1].forename} ${authors[1].surname}, `;
        }
        return `${authors[0].forename} ${authors[0].surname}, `;
      };
      const displayPage = (page: string | null) => {
        if (page) {
          return `, ${page}`;
        }
        return '';
      };
      return (
        <>
          {title}
          <p>
            {displayAuthors(imageSource?.book.authors)}
            <em>{imageSource?.book.title}</em>
            {`, ${imageSource?.book.town}, ${imageSource?.book.publisher}, ${imageSource.book.year}`}
            {displayPage(imageSource?.book.page)}
            .
          </p>
        </>
      );
    }
    return null;
  };

  return (
    <div className={STYLES.sources}>
      { displayImageSource(source) }
    </div>
  );
}
