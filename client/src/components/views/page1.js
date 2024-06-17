import '../Styles/page1.css'

function Page1(){
    return(
        <div className="features-container">
            <div className="features-header">
                <h1>Features</h1>
                <p>Discover the powerfull features of the Green Carbon Tracker</p>
            </div>
            <div className="features-grid">
                <div className='feature-card'>
                    <div className="feature-card1">
                        <h2>Real-time Tracking</h2>
                        <p>Monitor your carbon emissions in real-time and make informed decisions</p>
                    </div>
                    <div className="feature-card1">
                        <h2>Customizable Dashboard</h2>
                        <p>Personalize yourdashboard to display the information that matters most to you</p>
                    </div>
                </div>
                <div className='feature-card'>
                    <div className="feature-card2">
                        <h2>Goal Setting</h2>
                        <p>Set goals to reduce your carbon footprint and track your progress</p>
                    </div>
                    <div className="feature-card2">
                        <h2>Carbon Offset Suggestions</h2>
                        <p>Receive personalized suggestions on how to offset your carbon emissions</p>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Page1