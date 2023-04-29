import { render } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ReactElement } from 'react';
import { BrowserRouter } from 'react-router-dom';

const renderWithRouter = (ui: ReactElement, { route = '/' } = {}) => {
  window.history.pushState({}, 'Test page', route);
  const user = userEvent.setup();

  return {
    user,
    ...render(ui, { wrapper: BrowserRouter }),
  };
};

export * from '@testing-library/react';
export { renderWithRouter as render };