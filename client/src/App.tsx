import './App.scss';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { HomeContainer } from './containers/Home/HomeContainer';
import { ProfileContainer } from './containers/Profile/ProfileContainer';
import { RollContainer } from './containers/Roll/RollContainer';

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomeContainer />} />
        <Route path="/roll" element={<RollContainer />} />
        <Route path="/roll/:id" element={<ProfileContainer />} />
        {/* <Route component={ErrorPage}/> */}
      </Routes>
    </BrowserRouter>
  );
}
