import {
  Date, DeathPlace, Death, DeathCause, Cemetery,
} from '../../types/tunneller';

const mockDate: Date = {
  year: '1926',
  dayMonth: '13 October',
};

const mockPlace: DeathPlace = {
  location: 'Telegraph Hill',
  town: 'Arras',
  country: 'France',
};

const mockCause: DeathCause = {
  type: 'Killed in action',
  circumstances: 'Dead wounded by shell fire',
};

const mockCemetery: Cemetery = {
  name: 'Faubourg d\'Amiens',
  location: 'Arras',
  country: 'France',
  graveReference: 'IE 18',
};

export const mockDeath: Death = {
  date: mockDate,
  place: mockPlace,
  cause: mockCause,
  cemetery: mockCemetery,
  ageAtDeath: 89,
};
