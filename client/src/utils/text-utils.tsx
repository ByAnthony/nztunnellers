export const formatText = (text: string) => {
  const paragraphs = text.split('\\n\\n');
  let segmentKey: number = 0;
  return paragraphs.map((paragraph) => {
    const segments = paragraph
      .replace(/--/g, '\u00A0')
      .split(/(\*.+?\*)|(\[.+?\))/g);
    const formattedSegments = segments.map((segment) => {
      segmentKey += 1;
      if (segment && segment.startsWith('*') && segment.endsWith('*')) {
        const italicText = segment.slice(1, -1);
        return <em key={segmentKey}>{italicText}</em>;
      }
      if (segment && segment.startsWith('[') && segment.endsWith(')')) {
        const linkText = segment.slice(1, -1);
        const [label, url] = linkText.split('](');
        const number = label.slice(0, -1);
        if (url.includes('footnote')) {
          return (
            <a key={segmentKey} href={url} id={`reference_${number}`}>
              [
              {label}
              ]
            </a>
          );
        }
        return (
          <a key={segmentKey} href={url} id={`footnote_${number}`}>
            {label}
          </a>
        );
      }
      return <span key={segmentKey}>{segment}</span>;
    });
    return <p key={paragraphs.indexOf(paragraph)}>{formattedSegments}</p>;
  });
};
