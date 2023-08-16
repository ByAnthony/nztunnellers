import STYLES from './Title.module.scss';

type Props = {
  title: string;
  chapter: number;
}

export function Title({ title, chapter }: Props) {
  const [titleLine1, titleLine2] = title.split('\\');

  return (
    <>
      <div className={STYLES['main-title']}>
        <h1>
          <span className={STYLES['title-line-1']}>{titleLine1}</span>
          <span className={STYLES['title-line-2']}>{titleLine2}</span>
        </h1>
      </div>
      <p className={STYLES['title-line-3']}>{`Chapter ${chapter}`}</p>
    </>
  );
}
