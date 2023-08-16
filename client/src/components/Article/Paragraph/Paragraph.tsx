import { formatText } from '../../../utils/text-utils';

import { Section } from '../../../types/article';

import STYLES from './Paragraph.module.scss';

type Props = {
    section: Section;
}

export function Paragraph({ section }: Props) {
  return (
    <div className={STYLES.paragraph}>
      <h2>{section.title}</h2>
      {formatText(section.text)}
    </div>
  );
}
