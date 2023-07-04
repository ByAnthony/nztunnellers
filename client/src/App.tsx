import { useLayoutEffect } from 'react';
import {
  BrowserRouter, Route, Routes, useLocation,
} from 'react-router-dom';
import { CallToPickAndShovel } from './components/History/CallToPickAndShovel/CallToPickAndShovel';
import { HomePage } from './components/HomePage/HomePage';
import { Profile } from './components/Profile/Profile';
import { Roll } from './components/Roll/Roll';
import { Timeline } from './components/Timeline/Timeline';

const Wrapper = ({ children }: any) => {
  const location = useLocation();
  useLayoutEffect(() => {
    document.documentElement.scrollTo(0, 0);
  }, [location.pathname]);
  return children;
};

export function App() {
  return (
    <BrowserRouter>
      <Wrapper>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/history" />
          <Route path="/history/call-to-pick-and-shovel" element={<CallToPickAndShovel />} />
          <Route path="/tunnellers" element={<Roll />} />
          <Route path="/tunnellers/:id" element={<Profile />} />
          <Route path="/tunnellers/:id/wwi-timeline" element={<Timeline />} />
          {/* <Route component={ErrorPage}/> */}
        </Routes>
      </Wrapper>
    </BrowserRouter>
  );
}
