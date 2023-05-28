import { Birth, Origins, Parents } from '../../types/tunneller';

export const mockBirth = (overrides: Partial<Birth> | undefined = undefined): Birth => ({
  date: {
    year: '1886',
    dayMonth: '18 December',
  },
  country: 'New Zealand',
  ...overrides,
});

export const mockParents = (overrides: Partial<Parents> | undefined = undefined): Parents => ({
  mother: {
    name: 'Jane Doe',
    origin: 'New Zealand',
  },
  father: {
    name: 'John Doe',
    origin: 'Scotland',
  },
  ...overrides,
});

export const mockOrigins = (overrides: Partial<Origins>
    | undefined = undefined): Origins => ({
  birth: mockBirth(),
  parents: mockParents(),
  inNzLength: null,
  ...overrides,
});
