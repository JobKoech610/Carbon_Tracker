
import './App.css';

import SignUp from './components/views/signUp';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from './components/views/HomePage';
import Login from './components/views/Login';
import { UserProvider } from './components/views/UserContext';

function App() {
  return (
    <UserProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/signUp" element={<SignUp />} />
          <Route path="/Login" element={ <Login />} />

        </Routes>
       
      </Router>

      
      </UserProvider>
  );
}

export default App;
