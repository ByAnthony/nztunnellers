import { Section } from '../../../types/article';
import STYLES from '../History.module.scss';

type Props = {
    section: Section;
}

export const formatText = (text: string) => {
  const paragraphs = text.split('\\n\\n');
  return paragraphs.map((paragraph) => (
    <p key={paragraphs.indexOf(paragraph)}>
      {paragraph
        .replace(/--/g, '\u00A0')
        .split(/(\*.+?\*)|(\[.+?\))/g)
        .map((segment) => {
          if (segment && segment.startsWith('*') && segment.endsWith('*')) {
            const italicText = segment.slice(1, -1);
            return <em key={paragraph.indexOf(segment)}>{italicText}</em>;
          }
          if (segment && segment.startsWith('[') && segment.endsWith(')')) {
            const linkText = segment.slice(1, -1);
            const [label, url] = linkText.split('](');
            if (url.includes('footnote')) {
              return (
                <a key={paragraph.indexOf(segment)} href={url} id={`reference_${label}`}>
                  [
                  {label}
                  ]
                </a>
              );
            }
            const number = label.slice(0, -1);
            return (
              <a key={paragraph.indexOf(segment)} href={url} id={`footnote_${number}`}>
                {label}
              </a>
            );
          }
          return <span key={paragraph.indexOf(segment)}>{segment}</span>;
        })}
    </p>
  ));
};

export function Paragraph({ section }: Props) {
  return (
    <div className={STYLES.paragraph}>
      <h2>{section.title}</h2>
      {formatText(section.text)}
    </div>
  );
}
