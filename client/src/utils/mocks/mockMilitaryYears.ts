import {
  Date, DeathPlace, Death, DeathCause, Cemetery, Medal,
} from '../../types/tunneller';

const mockVictoryMedal: Medal = {
  name: 'Victory Medal',
  country: 'United Kingdom',
  image: 'victory-medal.png',
  citation: null,
};

export const mockBritishWarMedal: Medal = {
  name: 'British War Medal',
  country: 'United Kingdom',
  image: 'british-war-medal.png',
  citation: null,
};

export const mockMedals: Medal[] = [
  mockVictoryMedal,
  mockBritishWarMedal,
];

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
