import {BrowserRouter, Routes, Route} from "react-router-dom";
import "./App.css";
import {HomeContainer} from "../Home/HomeContainer";
import {CompanyRollContainer} from "../CompanyRoll/CompanyRollContainer";

const App = () => {
  return (
    <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomeContainer />}/>
          <Route path="/roll" element={<CompanyRollContainer />}/>
          {/* <Route component={ErrorPage}/> */}
        </Routes>
    </BrowserRouter>
  );
};

export default App;
