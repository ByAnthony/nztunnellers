import { ArmyExperience, Employment, PreWayYears } from '../../types/tunneller';

export const mockArmyExperience = (overrides: Partial<ArmyExperience>
    | undefined = undefined): ArmyExperience => ({
  unit: 'NZ Infantry',
  country: 'New Zealand',
  conflict: null,
  duration: '12 months',
  ...overrides,
});

export const mockEmployment = (overrides: Partial<Employment>
    | undefined = undefined): Employment => ({
  occupation: 'Goldminer',
  employer: 'Goldmining Company',
  ...overrides,
});

export const mockPreWarYears = (overrides: Partial<PreWayYears>
    | undefined = undefined): PreWayYears => ({
  armyExperience: [mockArmyExperience()],
  employment: mockEmployment(),
  residence: null,
  maritalStatus: null,
  wife: null,
  religion: null,
  ...overrides,
});
