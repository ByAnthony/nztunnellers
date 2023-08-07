import { Image, Next, Section } from '../../types/article';

export const mockTitle: string = 'My Awesome\\Article Title';

export const mockChapter: number = 1;

export const mockImage: Image = {
  file: 'img-123.png',
  alt: 'Accessible alt text',
};

export const mockSection: Section = {
  title: 'Section Title',
  text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea *commodo consequat*. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n\\nLorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat[1](#footnote_1). Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\\n\\n(6--July 2023)',
};

export const mockNextButton: Next = {
  url: 'my-path-to-next-chapter/',
  title: 'Next\\Chapter',
  chapter: 3,
};

export const mockNotes: string = '[1.](#reference_1) Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\\n\\n[2.](#reference_2) Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.';
