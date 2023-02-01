import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HomeContainer } from '../Home/HomeContainer';
import { RollContainer } from '../Roll/RollContainer';
import './App.scss';
import { TunnellerProfile } from '../../components/TunnellerProfile/TunnellerProfile';
import { useDispatch } from 'react-redux';
import { useEffect } from 'react';
import { getRoll } from '../../redux/actions/getRoll';


export function App() {

  const dispatch = useDispatch();

  useEffect(() => {
      getRoll().then((result) =>
      dispatch({ type: "roll", payload: result }))
  }, [dispatch]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomeContainer />} />
        <Route path="/roll" element={<RollContainer />} />
        <Route path="/roll/:id" element={<TunnellerProfile />} />
        {/* <Route component={ErrorPage}/> */}
      </Routes>
    </BrowserRouter>
  );
}
