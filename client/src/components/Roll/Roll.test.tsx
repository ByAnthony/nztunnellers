import '@testing-library/jest-dom/extend-expect';
import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { mockRoll } from '../../utils/mocks/mockRoll';
import { useGetAllTunnellersQuery } from '../../redux/slices/rollSlice';
import { Roll } from './Roll';

jest.mock('../../redux/slices/rollSlice', () => ({
  useGetAllTunnellersQuery: jest.fn(),
}));

describe('Profile', () => {
  it('renders profile when data is available', () => {
    (useGetAllTunnellersQuery as jest.Mock).mockReturnValue({
      data: mockRoll,
      error: null,
      isLoading: false,
      isSuccess: true,
    });

    const { asFragment } = render(
      <MemoryRouter>
        <Roll />
      </MemoryRouter>,
    );

    expect(asFragment()).toMatchSnapshot();

    const buttonD = screen.getByLabelText('Filter names by the letter D.');
    const buttonL = screen.getByLabelText('Filter names by the letter L.');
    const buttonR = screen.getByLabelText('Filter names by the letter R.');
    expect(buttonD).toBeInTheDocument();
    expect(buttonD).toHaveTextContent('D');
    expect(buttonL).toBeInTheDocument();
    expect(buttonL).toHaveTextContent('L');
    expect(buttonR).toBeInTheDocument();
    expect(buttonR).toHaveTextContent('R');

    const buttonAll = screen.getByLabelText('Remove the filter by name.');
    expect(buttonAll).toBeInTheDocument();
    expect(buttonAll).toHaveTextContent('All');

    const titleD = screen.getByLabelText('Letter D');
    const titleL = screen.getByLabelText('Letter L');
    const titleR = screen.getByLabelText('Letter R');
    expect(titleD).toHaveClass('title');
    expect(titleD).toHaveTextContent('D');
    expect(titleD).toBeInTheDocument();
    expect(titleL).toHaveClass('title');
    expect(titleL).toHaveTextContent('L');
    expect(titleL).toBeInTheDocument();
    expect(titleR).toHaveClass('title');
    expect(titleR).toHaveTextContent('R');
    expect(titleR).toBeInTheDocument();

    expect(screen.getByText('John')).toBeInTheDocument();
    expect(screen.getByText('Doe')).toBeInTheDocument();

    expect(screen.getByText('Alexander')).toBeInTheDocument();
    expect(screen.getByText('Driscott')).toBeInTheDocument();

    expect(screen.getByText('Robert')).toBeInTheDocument();
    expect(screen.getByText('Lang')).toBeInTheDocument();

    expect(screen.getByText('William')).toBeInTheDocument();
    expect(screen.getByText('Right')).toBeInTheDocument();
  });

  it('does not render profile when data is undefined', () => {
    (useGetAllTunnellersQuery as jest.Mock).mockReturnValue({
      data: undefined,
      error: null,
      isLoading: false,
      isSuccess: true,
    });

    const { container } = render(<Roll />);

    expect(container).toBeEmptyDOMElement();
  });
});
