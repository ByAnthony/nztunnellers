import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.scss';
import { HomeContainer } from './containers/Home/HomeContainer';
import { RollContainer } from './containers/Roll/RollContainer';
import { ProfileContainer } from './containers/Profile/ProfileContainer';

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
