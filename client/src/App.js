import logo from './logo.svg';
import './App.css';
import Page4 from './components/views/page4';
import Page2 from './components/views/page2';
import Page1 from './components/views/page1';
import FAQ from './components/views/FAQ';
import Landing from './components/views/Landing';
import Contact from './components/views/Contact';
function App() {
  return (
    <div>
      <Landing />
      <Page1 />
      <Page2 />
      <Page4 />
      <FAQ />
      <Contact />
    </div>
  );
}

export default App;
