import '@testing-library/jest-dom';
import { render } from '@testing-library/react';
import { mockBirth } from '../../utils/mocks/mockOrigins';
import { DiaryBirth } from './DiaryBirthInfo';

test('renders the component correctly', () => {
  const component = (
    <DiaryBirth birth={mockBirth()} />
  );
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});
