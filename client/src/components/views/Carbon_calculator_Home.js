import React, { useState } from 'react';

function Carbon_calculator_Home() {
  const [formData, setFormData] = useState({
    electricity: '',
    cookingGas: '',
    diesel: '',
    coal: '',
    biomass: ''
  });

  const [totalEmissions, setTotalEmissions] = useState(null);
  const [offsetsNeeded, setOffsetsNeeded] = useState(null);
  const [costOffset, setPurchaseOffsets] = useState(null)

  const emissionFactors = {
    electricity: 0.92, // kg CO₂e per kWh (U.S. average)
    cookingGas: 5.3,   // kg CO₂e per therm
    diesel: 10.21,     // kg CO₂e per gallon
    coal: 2.86,        // kg CO₂e per kg
    biomass: 0.44      // kg CO₂e per pound
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const calculateEmissions = (data) => {
    const emissions = {
      electricity: data.electricity * emissionFactors.electricity,
      cookingGas: data.cookingGas * emissionFactors.cookingGas,
      diesel: data.diesel * emissionFactors.diesel,
      coal: data.coal * emissionFactors.coal,
      biomass: data.biomass * emissionFactors.biomass
    };

    const total = Object.values(emissions).reduce((acc, val) => acc + (isNaN(val) ? 0 : val), 0);
    return total;
  };

  const calculateOffsetsNeeded = (totalEmissions) => {
    return totalEmissions / 1000; // Convert kg CO₂e to metric tons
  };

  const purchaseOffsets = (totalEmissions, pricePerTon) => {
    return (totalEmissions / 1000) * pricePerTon;
  };

  

  const handleSubmit = (e) => {
    e.preventDefault();
    const totalEmissions = calculateEmissions(formData);
    setTotalEmissions(totalEmissions);

    const offsets = calculateOffsetsNeeded(totalEmissions);
    setOffsetsNeeded(offsets);

    const pricePerTon = 10; // USD per metric ton CO₂e
  const offsetCost = purchaseOffsets(totalEmissions, pricePerTon);
  setPurchaseOffsets(offsetCost)
  };

  return (
    <div>
      <h3>Carbon Calculator</h3>
      <div>
        <form onSubmit={handleSubmit}>
          <label>Electricity (kWh)</label>
          <input type='number' name='electricity' value={formData.electricity} onChange={handleChange} />
          <label>Cooking Gas (therms)</label>
          <input type='number' name='cookingGas' value={formData.cookingGas} onChange={handleChange} />
          <label>Diesel (gallons)</label>
          <input type='number' name='diesel' value={formData.diesel} onChange={handleChange} />
          <label>Coal (kg)</label>
          <input type='number' name='coal' value={formData.coal} onChange={handleChange} />
          <label>Biomass (pounds)</label>
          <input type='number' name='biomass' value={formData.biomass} onChange={handleChange} />
          
          <button type='submit'>Submit</button>
        </form>
      </div>

      {totalEmissions !== null && (
        <div>
          <h4>Total Carbon Emissions: {totalEmissions.toFixed(2)} kg CO₂e</h4>
          <h4>Carbon Offsets Needed: {offsetsNeeded.toFixed(2)} metric tons</h4>
          <h4>To Offsets your carbon footprint it costs: {`USD ${costOffset}`}</h4>
          <p>To offset this carbon footprint, you can consider actions like planting trees, investing in renewable energy, or purchasing carbon offsets.</p>
        </div>
      )}
    </div>
  );
}

export default Carbon_calculator_Home;
