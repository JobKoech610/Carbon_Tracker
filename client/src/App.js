
import './App.css';

import SignUp from './components/views/signUp';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from './components/views/HomePage';



function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={< HomePage/>} />
          <Route path="/signUp" element={<SignUp />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
