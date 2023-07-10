import STYLES from '../History.module.scss';

type Props = {
  title: string;
  chapter: number;
}

export function Title({ title, chapter }: Props) {
  const [titleLine1, titleLine2] = title.split('\\');

  return (
    <div className={STYLES['chapter-title']}>
      <h1>
        <span className={STYLES['sub-title']}>{titleLine1}</span>
        <span className={STYLES.title}>{titleLine2}</span>
      </h1>
      <div className={STYLES['chapter-number']}>{chapter}</div>
    </div>
  );
}
