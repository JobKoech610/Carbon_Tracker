import React, { useState, useEffect } from 'react';
import axios from 'axios';

const emissionFactors = {
  natural_gas: 5.3,  // kg CO₂e per therm
  diesel: 10.21,     // kg CO₂e per gallon
  gasoline: 8.89,    // kg CO₂e per gallon
  electricity: 0.92, // kg CO₂e per kWh (U.S. average)
  air_travel: 0.217, // kg CO₂e per mile (average for medium-haul flights)
  waste: 0.44        // kg CO₂e per pound
};


function Page3(){

    const [data, setData] = useState(null);
    const [emissions, setEmissions] = useState(null);
    const [totalEmissions, setTotalEmissions] = useState(0);
  
    useEffect(() => {
      // Fetch data from the backend
      axios.get('http://127.0.0.1:5000/fact-calc')
        .then(response => {
          setData(response.data);
          calculateEmissions(response.data);
        })
        .catch(error => {
          console.error("Error fetching data:", error);
        });
        console.log(data)
    }, []);
  
    const calculateEmissions = (consumption) => {
      const emissions = {};
      let total = 0;
  
      for (const [category, amount] of Object.entries(consumption)) {
        const emission = amount * emissionFactors[category];
        emissions[category] = emission;
        total += emission;
      }
  
      setEmissions(emissions);
      setTotalEmissions(total);
    };
  
    const purchaseOffsets = (totalEmissions, pricePerTon) => {
      return (totalEmissions / 1000) * pricePerTon;
    };
  
    const pricePerTon = 10; // USD per metric ton CO₂e
    const offsetCost = purchaseOffsets(totalEmissions, pricePerTon);
  
    return(
        // <div>
        //     <h1>Emission Tracking Dashboard</h1>
        //     <p>Display a user-friendly dashboard where users can track their emissions and view their carbon footprint</p>
        // </div>
        <div className="App">
            <h1>Emission Tracking Dashboard</h1>
                {emissions ? (
                <div>
                    <h2>Annual Emissions (kg CO₂e):</h2>
                    <ul>
                    {Object.entries(emissions).map(([category, emission]) => (
                        <li key={category}>
                        {capitalizeFirstLetter(category)}: {emission.toFixed(2)} kg CO₂e
                        </li>
                    ))}
                    </ul>
                    <h3>Total Emissions: {totalEmissions.toFixed(2)} kg CO₂e ({(totalEmissions / 1000).toFixed(2)} metric tons CO₂e)</h3>
                    <h3>Cost to offset emissions: ${offsetCost.toFixed(2)}</h3>
                </div>
                ) : (
                <p>Loading data...</p>
                )}
        </div>
    )
}

const capitalizeFirstLetter = (string) => {
    return string.charAt(0).toUpperCase() + string.slice(1);
  };

export default Page3