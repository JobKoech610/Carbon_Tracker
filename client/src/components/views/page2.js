import React from 'react';
import '../Styles/page2.css'

function Page2() {
    return (
        <div className="how-it-works-container">
            <div className="how-it-works-header">
                <h1>How It Works</h1>
                <p>Illustrates the process of tracking emissions using the Green Carbon Tracker, highlighting the steps involved</p>
            </div>
            <div className="steps-grid">
                <div className="step-card">
                    <div className="step-number">1</div>
                    <h2>Step 1: Sign Up</h2>
                    <p>Sign up for an account on the Green Carbon Tracker platform, providing basic information</p>
                </div>
                <div className="step-card">
                    <div className="step-number">2</div>
                    <h2>Step 2: Set up your profile</h2>
                    <p>Provide information about your location, transportation methods, and energy usage to calculate your carbon footprint</p>
                </div>
                <div className="step-card">
                    <div className="step-number">3</div>
                    <h2>Step 3: Track your activities</h2>
                    <p>Use the Green Carbon Tracker to log your daily activities that contribute to carbon emissions such as driving, flying, or using electricity</p>
                </div>
                <div className="step-card">
                    <div className="step-number">4</div>
                    <h2>Step 4: Monitor your progress</h2>
                    <p>View detailed reports and visualization of your carbon footprint over time to understand the impact of your actions</p>
                </div>
                <div className="step-card">
                    <div className="step-number">5</div>
                    <h2>Step 5: Take action</h2>
                    <p>Receive personalized recommendations and tips on how to reduce your carbon footprint and contribute to a greener future</p>
                </div>
            </div>
        </div>
    );
}

export default Page2;