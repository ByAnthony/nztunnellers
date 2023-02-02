import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { HomeContainer } from '../Home/HomeContainer';
import { RollContainer } from '../Roll/RollContainer';
import './App.scss';
import { TunnellerProfile } from '../../components/TunnellerProfile/TunnellerProfile';

export function App() {

  // const dispatch: AppDispatch = useDispatch()

  // useEffect(() => {
  //     dispatch(getRoll())
  // }, [dispatch]);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomeContainer />} />
        <Route path="/roll" element={<RollContainer />} />
        {/* <Route path="/roll/:id" element={<TunnellerProfile />} /> */}
        {/* <Route component={ErrorPage}/> */}
      </Routes>
    </BrowserRouter>
  );
}
