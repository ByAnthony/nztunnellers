import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { mockSources } from '../../utils/mocks/mockSources';
import { ProfileSources } from './ProfileSources';

const component = <ProfileSources sources={mockSources()} />;

test('renders the component correctly', () => {
  const { asFragment } = render(component);

  expect(asFragment()).toMatchSnapshot();
});

test('renders Auckland War Memorial Museum information', () => {
  render(component);

  expect(screen.getByTestId('awmm')).toHaveTextContent('Auckland War Memorial Museum Tāmaki Paenga Hira: Online Cenotaph He Toa Taumata Rau.');
  expect(screen.getByRole('link', { name: 'Online Cenotaph He Toa Taumata Rau' })).toHaveAttribute('href', 'https://www.mockurl.co.nz/online-cenotaph/B2874930');
});

test('renders NZ Archives information', () => {
  render(component);

  expect(screen.getByTestId('nz-archives')).toHaveTextContent('New Zealand Archives Te Rua Mahara o te Kāwanatanga, AABK 18805 W5530 39/0022386, Military Personnel File');
  expect(screen.getByRole('link', { name: 'Military Personnel File' })).toHaveAttribute('href', 'https://www.mockurl.co.nz/online-cenotaph/B2874930');
});

test('renders London Gazette information', () => {
  render(component);

  expect(screen.getByTestId('london-gazette')).toHaveTextContent('London Gazette, 23 May 1917, p. 1675.');
});

test('renders Nominal Roll information', () => {
  render(component);

  expect(screen.getByTestId('nominal-roll'))
    .toHaveTextContent('Nominal Roll of New Zealand Expeditionary Force, 1915. New Zealand Engineers Tunnelling Company, Government Printer, Wellington, 1916, 37.');
});

test('renders Nominal Roll with volume and roll information', () => {
  const componentWithNominalRoll = (
    <ProfileSources sources={mockSources({
      nominalRoll: {
        title: 'Nominal Rolls of New Zealand Expeditionary Force',
        town: 'Wellington',
        publisher: 'Government Printer',
        date: '1916',
        page: '37',
        volume: 'Volume III',
        roll: 'No.55',
      },
    })}
    />
  );

  render(componentWithNominalRoll);

  expect(screen.getByTestId('nominal-roll')).toHaveTextContent('Nominal Rolls of New Zealand Expeditionary Force, Volume III, No.55, Government Printer, Wellington, 1916, 37.');
});
