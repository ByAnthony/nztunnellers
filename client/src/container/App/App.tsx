import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomeContainer } from "../Home/HomeContainer";
import { RollContainer } from "../Roll/RollContainer";
import "./App.css";

export const App = () => {
  return (
    <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomeContainer />}/>
          <Route path="/roll" element={<RollContainer />}/>
          {/* <Route component={ErrorPage}/> */}
        </Routes>
    </BrowserRouter>
  );
};
