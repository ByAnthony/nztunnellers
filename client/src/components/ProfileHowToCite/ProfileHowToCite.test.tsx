import { render } from '@testing-library/react';
import { Summary } from '../../types/tunneller';
import { ProfileHowToCite } from './ProfileHowToCite';

test('renders the component', () => {
  const testId = 26;
  const testSummary: Summary = {
    serial: '12345',
    name: {
      forename: 'John',
      surname: 'Doe',
    },
    birth: '1888',
    death: '1975',
  };

  const { asFragment } = render(
    <ProfileHowToCite id={testId} summary={testSummary} />,
  );

  expect(asFragment()).toMatchSnapshot();
});
