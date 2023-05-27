import {
  Image, ImageSource, ImageNewspaper, ImageArchives, ImageBook,
} from '../../types/tunneller';

export const mockImageAucklandLibraries: string = 'https://digitalnz.org/records?text=31-B2671&tab=Images#';

export const mockImageArchives: ImageArchives = {
  location: 'Auckland War Memorial Museum',
  reference: 'MS-93/157',
};

export const mockImageFamily: string = 'John Doe family';

export const mockImageNewspaper: ImageNewspaper = {
  name: 'Auckland Star',
  date: '12 July 1898',
};

export const mockImageBook = (overrides: Partial<ImageBook>
    | undefined = undefined): ImageBook => ({
  title: 'My Mock Title',
  town: 'Bethune',
  publisher: 'Publisher and Co.',
  authors: [
    {
      forename: 'Jane',
      surname: 'Doe',
    },
  ],
  year: '1925',
  page: '89',
  ...overrides,
});

const mockSource = (overrides: Partial<ImageSource> | undefined = undefined): ImageSource => ({
  aucklandLibraries: null,
  archives: null,
  family: null,
  newspaper: null,
  book: null,
  ...overrides,
});

export const mockImages = (overrides: Partial<Image> | undefined = undefined): Image => ({
  url: '',
  source: mockSource(),
  ...overrides,
});
