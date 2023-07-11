import STYLES from '../Notes/Notes.module.scss';

type Props = {
  title: string;
  today: Date;
};

export function HowToCite({ title, today }: Props) {
  return (
    <div className={STYLES.notes}>
      <h3>How to cite this page</h3>
      <p>
        Anthony Byledbal, &ldquo;
        {title.replace('\\', ' ')}
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
  );
}
