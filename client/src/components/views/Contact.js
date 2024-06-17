import React from 'react';
import '../Styles/Contact.css';

function Contact() {
  return (
    <div className='contact-container'>
        <div className='contact-info'>
            <h2>Contact Us</h2>
            <div className='contact-details'>
                <div className='contact-item'>
                    <h3>Email</h3>
                    <p>info@greencarbontracker.com</p>
                </div>
                <div className='contact-item'>
                    <h3>Phone</h3>
                    <p>+254708810442</p>
                </div>
                <div className='contact-item'>
                    <h3>Address</h3>
                    <p>Nairobi City,</p>
                </div>
            </div>
            {/* <button className='submit-button'>Submit</button> */}
        </div>
        <div className='contact-form'>
            <h3>Get In Touch</h3>
            <form>
                <div className='form-group'>
                    <label>First Name</label>
                    <input type="text" placeholder="John"/>
                </div>
                <div className='form-group'>
                    <label>Surname</label>
                    <input type="text" placeholder='Doe'/>
                </div>
                <div className='form-group'>
                    <label>E-mail</label>
                    <input type='email' placeholder='email'/>
                </div>
                <div className='form-group'>
                    <label>Address</label>
                    <input type="text" placeholder='Nairobi'/>
                </div>
                <div className='form-group'>
                    <label>Description</label>
                    <textarea rows='4'></textarea>
                </div>
                <button type="submit" className='submit-button'>Submit</button>
            </form>
        </div>
    </div>
  );
}

export default Contact;
