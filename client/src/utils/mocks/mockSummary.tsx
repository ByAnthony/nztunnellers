import { Summary } from '../../types/tunneller';

export const mockSummary = (overrides: Partial<Summary> | undefined = undefined): Summary => ({
  serial: '1/2345',
  name: {
    forename: 'John',
    surname: 'Doe',
  },
  birth: '1888',
  death: '1975',
  ...overrides,
});
