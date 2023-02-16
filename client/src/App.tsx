import './App.scss';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { HomeContainer } from './components/HomeContainer/HomeContainer';
import { RollContainer } from './components/RollContainer/RollContainer';
import { ProfileContainer } from './components/ProfileContainer/ProfileContainer';

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
