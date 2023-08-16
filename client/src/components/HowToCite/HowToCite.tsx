import { displayBirthDeathDates } from '../../utils/utils';
import type { Summary } from '../../types/tunneller';
import STYLES from './HowToCite.module.scss';

type HowToCiteUrlProps = {
  id: number | undefined;
  title: string | undefined;
};

function HowToCiteUrl({ id, title }: HowToCiteUrlProps) {
  if (id) {
    return <span>{`URL: www.nztunnellers.com/tunnellers/${id}.`}</span>;
  }
  const articleTitle = title?.replace('\\', '-').replace(' ', '-').toLowerCase();
  return <span>{`URL: www.nztunnellers.com/history/${articleTitle}.`}</span>;
}

type HowToCiteTitleProps = {
  tunneller: Summary | undefined;
  title: string | undefined;
};

function HowToCiteTitle({ tunneller, title }: HowToCiteTitleProps) {
  if (tunneller) {
    return (
      <>
        {`${tunneller.name.forename} ${tunneller.name.surname} `}
        {`(${displayBirthDeathDates(tunneller.birth, tunneller.death)})`}
      </>
    );
  }
  const articleTitle = title?.replace('\\', ' ');
  return <span>{articleTitle}</span>;
}

type Props = {
  id?: number;
  summary?: Summary;
  title?: string;
  today: Date;
};

export function HowToCite({
  id, summary, title, today,
}: Props) {
  return (
    <div className={STYLES.howtocite}>
      <h3>How to cite this page</h3>
      <p>
        Anthony Byledbal, &ldquo;
        <HowToCiteTitle tunneller={summary} title={title} />
        &ldquo;,
        <em> New Zealand Tunnellers Website</em>
        {`, ${today.getFullYear()} (2009), Accessed: `}
        {`${today.toLocaleDateString('en-NZ', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        })}. `}
        <HowToCiteUrl id={id} title={title} />
      </p>
    </div>
  );
}

HowToCite.defaultProps = {
  id: null,
  summary: null,
  title: null,
};
