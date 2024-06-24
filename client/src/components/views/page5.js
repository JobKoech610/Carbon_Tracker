import React, { useState } from 'react';
import CarbonCalculatorFactory from './CarbonCalculatorFactory';
import CarbonCalculatorHome from './CarbonCalculatorHome';
import '../Styles/page5.css';

function Page5() {
    const [currentPage, setCurrentPage] = useState('home');

    const switchPage = (page) => {
        setCurrentPage(page);
    };

    return (
        <div className="page-container">
            <h1>Carbon Offsetting</h1>
            <button>Offset your Emissions</button>

            <div className="switch-buttons">
                <div>
                    <button onClick={() => switchPage('home')}>Factory</button>
                </div>
                <div>
                    <button onClick={() => switchPage('factory')}>Home</button>
                </div>
            </div>

            <div className="calculator-container">
                {currentPage === 'home' && <CarbonCalculatorHome />}
                {currentPage === 'factory' && <CarbonCalculatorFactory />}
            </div>
        </div>
    );
}

export default Page5;
