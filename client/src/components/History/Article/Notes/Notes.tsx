import STYLES from './Notes.module.scss';
import { formatText } from '../Paragraph/Paragraph';

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
