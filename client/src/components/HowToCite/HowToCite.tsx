import { displayBiographyDates } from '../../utils/displayBiographyDates';

import type { Summary } from '../../types/tunneller';

import STYLES from './HowToCite.module.scss';

type HowToCiteUrlProps = {
  id: number | undefined;
  title: string | undefined;
};

type HowToCiteTitleProps = {
  tunneller: Summary | undefined;
  title: string | undefined;
};

type Props = {
  id?: number;
  summary?: Summary;
  title?: string;
  today: Date;
};

function HowToCiteUrl({ id, title }: HowToCiteUrlProps) {
  if (id) {
    return <span>{`URL: www.nztunnellers.com/tunnellers/${id}.`}</span>;
  }
  const articleTitle = title?.replace(/\s+|\\/g, '-').toLowerCase();
  return <span>{`URL: www.nztunnellers.com/history/${articleTitle}.`}</span>;
}

function HowToCiteTitle({ tunneller, title }: HowToCiteTitleProps) {
  if (tunneller) {
    return (
      <>
        {`${tunneller.name.forename} ${tunneller.name.surname} `}
        {`(${displayBiographyDates(tunneller.birth, tunneller.death)})`}
      </>
    );
  }
  const articleTitle = title?.replace('\\', ' ');
  return <span>{articleTitle}</span>;
}

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
