import React, { useState } from 'react';

function Carbon_calculator_Factory() {
  const [formData, setFormData] = useState({
    electricity: '',
    cookingGas: '',
    heating_oil: '',
    natural_gas: '',
    waste: '',
    vehicle: '',
    water: ''
  });

  const [totalEmissions, setTotalEmissions] = useState(null);
  const [offsetsNeeded, setOffsetsNeeded] = useState(null);
  const [costOffset, setPurchaseOffsets] = useState(null)

  const emissionFactors = {
    electricity: 0.92,    // kg CO₂e per kWh (U.S. average)
    natural_gas: 5.3,     // kg CO₂e per therm
    heating_oil: 10.21,   // kg CO₂e per gallon
    cookingGas: 5.75,        // kg CO₂e per gallon
    waste: 0.44,          // kg CO₂e per pound
    water: 0.001,         // kg CO₂e per gallon
    vehicle: 0.404        // kg CO₂e per mile
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
      heating_oil: data.heating_oil * emissionFactors.heating_oil,
      natural_gas: data.natural_gas * emissionFactors.natural_gas,
      waste: data.waste * emissionFactors.waste,
      vehicle: data.vehicle * emissionFactors.vehicle,
      water: data.water * emissionFactors.water
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
      <h3>Home Carbon Calculator</h3>
      <div>
        <form onSubmit={handleSubmit}>
          <label>Electricity (kWh)</label>
          <input type='number' name='electricity' value={formData.electricity} onChange={handleChange} />
          <label>Cooking Gas (therms)</label>
          <input type='number' name='cookingGas' value={formData.cookingGas} onChange={handleChange} />
          <label>heating_oil (Liters)</label>
          <input type='number' name='heating_oil' value={formData.heating_oil} onChange={handleChange} />
          <label>natural_gas (kg)</label>
          <input type='number' name='natural_gas' value={formData.natural_gas} onChange={handleChange} />
          <label>waste (pounds)</label>
          <input type='number' name='waste' value={formData.waste} onChange={handleChange} />
          <label>vehicle (Kilometers travelled)</label>
          <input type='number' name='vehicle' value={formData.vehicle} onChange={handleChange} />
          <label>water(pounds)</label>
          <input type='number' name='water' value={formData.water} onChange={handleChange} />
          <br/>
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

export default Carbon_calculator_Factory;