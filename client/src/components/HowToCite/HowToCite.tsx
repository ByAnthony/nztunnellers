import { displayBiographyDates } from '../../utils/displayBiographyDates';

import type { Summary } from '../../types/tunneller';

import STYLES from './HowToCite.module.scss';

type Props = {
  id?: number;
  summary?: Summary;
  title?: string;
  today: Date;
  timeline?: boolean;
};

type HowToCiteUrlProps = {
  id: number | undefined;
  title: string | undefined;
  timeline: boolean | undefined;
};

type HowToCiteTitleProps = {
  tunneller: Summary | undefined;
  title: string | undefined;
  timeline: boolean | undefined;
};

function HowToCiteUrl({ id, title, timeline = false }: HowToCiteUrlProps) {
  if (id) {
    if (!timeline) {
      return <span>{`URL: www.nztunnellers.com/tunnellers/${id}.`}</span>;
    }
    return <span>{`URL: www.nztunnellers.com/tunnellers/${id}/wwi-timeline.`}</span>;
  }

  const articleTitle = title?.replace(/\s+|\\/g, '-').toLowerCase();
  return <span>{`URL: www.nztunnellers.com/history/${articleTitle}.`}</span>;
}

function HowToCiteTitle({ tunneller, title, timeline = false }: HowToCiteTitleProps) {
  if (tunneller) {
    if (!timeline) {
      return (
        <>
          {`${tunneller.name.forename} ${tunneller.name.surname} `}
          {`(${displayBiographyDates(tunneller.birth, tunneller.death)})`}
        </>
      );
    }
    return (
      <>
        World War I Timeline of
        {` ${tunneller.name.forename} ${tunneller.name.surname} `}
      </>
    );
  }

  const articleTitle = title?.replace('\\', ' ');
  return <span>{articleTitle}</span>;
}

export function HowToCite({
  id, summary, title, today, timeline,
}: Props) {
  return (
    <div className={STYLES.howtocite}>
      <h3>How to cite this page</h3>
      <p>
        Anthony Byledbal, &ldquo;
        <HowToCiteTitle tunneller={summary} title={title} timeline={timeline} />
        &ldquo;,
        <em> New Zealand Tunnellers Website</em>
        {`, ${today.getFullYear()} (2009), Accessed: `}
        {`${today.toLocaleDateString('en-NZ', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
        })}. `}
        <HowToCiteUrl id={id} title={title} timeline={timeline} />
      </p>
    </div>
  );
}

HowToCite.defaultProps = {
  id: null,
  summary: null,
  title: null,
  timeline: false,
};
