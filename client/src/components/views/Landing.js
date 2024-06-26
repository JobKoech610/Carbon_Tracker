import React from 'react'
import '../Styles/Landing.css'
import image from '../../Assets/Carbont2.jpeg' 


function Landing() {
  return (
    <div className='container-l'>
        <div className='side-right'>
          <h1>Welcome to Green Carbon Tracker</h1>
          <p>Track, reduce, and offset your carbon emissions with ease.</p>
          <button className='btn'>Get started</button>
        </div>

        <div className='side-left'>
          <img src={image} alt="ILLUSTRATION"/>
        </div>
    </div>
  )
}

export default Landing