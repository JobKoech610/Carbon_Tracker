
import './App.css';
import Page4 from './components/views/page4';
import Page2 from './components/views/page2';
import Page1 from './components/views/page1';
import Page3 from './components/views/page3';
import Carbon_calculator_Factory from './components/views/Carbon_Calculator_Factory';

function App() {
  return (
    <div>
      <Carbon_calculator_Factory />
      <Page1 />
      <Page2 />
      <Page3 />
      <Page4 />
    </div>
  );
}

export default App;
