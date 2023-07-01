import { mockId } from './mockProfile';

const johnDoe = {
  forename: 'John',
  surname: 'Doe',
};

const alexanderDriscott = {
  forename: 'Alexander',
  surname: 'Driscott',
};

const williamRight = {
  forename: 'William',
  surname: 'Right',
};

const robertLang = {
  forename: 'Robert',
  surname: 'Lang',
};

export const mockDetails = {
  id: mockId,
  name: johnDoe,
  birth: '1886',
  death: '1952',
};

export const mockRoll = {
  D: [
    mockDetails,
    {
      ...mockDetails,
      id: 1,
      name: alexanderDriscott,
    },
  ],
  L: [
    {
      ...mockDetails,
      id: 2,
      name: robertLang,
    },
  ],
  R: [
    {
      ...mockDetails,
      id: 3,
      name: williamRight,
    },
  ],
};
