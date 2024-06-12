import React from 'react';
import '../Styles/page4.css'; // Import the CSS file

function Page4() {
    return (
        <div className="tips-container">
            <div className="tips-header">
                <h1>Tips for Reducing Emissions</h1>
                <p>Offers practical tips and suggestions for reducing carbon emissions, helping users make a positive impact</p>
            </div>
            <div className="tips-grid">
                <div className="tip-card">
                    <div className="tip-number">1</div>
                    <h2>Reduce Energy Consumption</h2>
                    <p>Turn off lights and appliances when not in use, use energy-efficient light bulbs, and insulate your home to reduce heating and cooling needs</p>
                </div>
                <div className="tip-card">
                    <div className="tip-number">2</div>
                    <h2>Choose Sustainable Transportation</h2>
                    <p>Opt for walking, cycling, or public transportation whenever possible. If you need to drive, carpool or choose a fuel-efficient vehicle</p>
                </div>
                <div className="tip-card">
                    <div className="tip-number">3</div>
                    <h2>Eat a Plant-Based Diet</h2>
                    <p>Reduce your meat and dairy consumption and opt for plant-based alternatives. Eating less meat can significantly reduce your carbon footprint</p>
                </div>
                <div className="tip-card">
                    <div className="tip-number">4</div>
                    <h2>Reduce, Reuse, Recycle</h2>
                    <p>Minimize waste by reducing your consumption, reusing items, and recycling materials. Choose products with minimal packaging and recycle whenever possible</p>
                </div>
                <div className="tip-card">
                    <div className="tip-number">5</div>
                    <h2>Support Renewable Energy</h2>
                    <p>Switch to renewable energy sources such as solar or wind power for your home or business. Consider investing in renewable energy projects</p>
                </div>
            </div>
        </div>
    );
}

export default Page4;
