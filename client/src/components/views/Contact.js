import React from 'react'
import '../Styles/Contact.css'

function Contact() {
  return (
    <div className='contact-container'>
        <div>
            <h2>Contact Us</h2>
            <div className=''>
            <div>
                <h3>Email</h3>
                <p></p>
            </div>
            <div>
                <h3>Phone</h3>
                <p>+254708810442</p>
            </div>
            <div>
                <h3>Address</h3>
                <p>Nairobi</p>
            </div>
            </div>
        </div>
        <div>
            <h3>Get In Touch</h3>
            <form>
                <label>First Name</label>
                <input type="text" placeholder="John"/>
                <label>Surname</label>
                <input type="text" placeholder='Doe'/>
                <label>E-mail</label>
                <input type='email' placeholder='johndoe@mail.net'/>
                <label>Address</label>
                <input type="text" placeholder='Nairobi'/>
                <label>Description</label>
                <textarea rows='4'></textarea>
                <button type="submit">Submit</button>
            </form>
        </div>
    </div>
  )
}

export default Contact