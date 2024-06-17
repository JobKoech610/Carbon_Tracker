
import './App.css';
import Page4 from './components/views/page4';
import Page2 from './components/views/page2';
import Page1 from './components/views/page1';
import Page3 from './components/views/page3';
import CarbonCalculatorFactory from './components/views/CarbonCalculatorFactory';
import CarbonCalculatorHome from './components/views/CarbonCalculatorHome';
import Landing from './components/views/Landing';
import FAQ from './components/views/FAQ';
import Contact from './components/views/Contact';
import Page5 from './components/views/page5';


function App() {
  return (
    <div>
      <Landing />
      <CarbonCalculatorHome />
      <CarbonCalculatorFactory />
      <Page1 />
      <Page2 />
      <Page3 />
      <Page4 />
      <Page5 />
      <FAQ />
      <Contact />
    </div>
  );
}

export default App;
