import { formatText } from '../../../utils/text-utils';

import STYLES from './Notes.module.scss';

type Props = {
    notes: string;
};

export function Notes({ notes }: Props) {
  return (
    <div className={STYLES.notes}>
      <h3>Notes</h3>
      {formatText(notes)}
    </div>
  );
}
