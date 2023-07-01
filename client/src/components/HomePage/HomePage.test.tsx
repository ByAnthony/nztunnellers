import '@testing-library/jest-dom';
import { HomePage } from './HomePage';
import { renderWithMemoryRouter } from '../../utils/test-utils';

const component = <HomePage />;

test('renders the component correctly', () => {
  const { asFragment } = renderWithMemoryRouter(component);

  expect(asFragment()).toMatchSnapshot();
});
