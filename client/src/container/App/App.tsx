import {BrowserRouter, Routes, Route} from "react-router-dom";
import "./App.css";
import HomeContainer from "../Home/HomeContainer";
import RollContainer from "../Roll/RollContainer";

const App = () => {
  return (
    <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomeContainer />}/>
          <Route path="/roll" element={<RollContainer />}/>
          {/* <Route component={ErrorPage}/> */}
        </Routes>
    </BrowserRouter>
  );
}

export default App;
