import CarbonCalculatorFactory from "./CarbonCalculatorFactory"
import CarbonCalculatorHome from "./CarbonCalculatorHome"
import { useState } from "react";

function Page5() {
    const [currentPage, setCurrentPage] = useState('home');

    const switchPage = (page) => {
        setCurrentPage(page);
    };

    return (
        <div>
            <h1>Carbon Offsetting</h1>
            <button>Offset your Emissions</button>

            <div>
                <div>
                    <button onClick={() => switchPage('home')}>Home</button>
                </div>
                <div>
                    <button onClick={() => switchPage('factory')}>Factory</button>
                </div>
            </div>

            <div>
                {currentPage === 'home' && <CarbonCalculatorHome />}
                {currentPage === 'factory' && <CarbonCalculatorFactory />}
            </div>
        </div>
    );
}

export default Page5;