import './App.scss';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { HomePage } from './components/HomePage/HomePage';
import { Profile } from './components/Profile/Profile';
import { Roll } from './components/Roll/Roll';

export function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/roll" element={<Roll />} />
        <Route path="/roll/:id" element={<Profile />} />
        <Route path="/roll/:id/wwi-timeline" />
        {/* <Route component={ErrorPage}/> */}
      </Routes>
    </BrowserRouter>
  );
}
