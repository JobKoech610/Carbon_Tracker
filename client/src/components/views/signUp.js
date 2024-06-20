import { useState } from "react";
import '../Styles/signup.css';

function SignUp() {
    const [formData, setFormData] = useState({
        name: "",
        phoneNumber: "",
        email: "",
        password: "",
    });

    const [error, setError] = useState("");

    const handleOnChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
        setError(""); // Clear error message on change
    };

    const validateForm = () => {
        if (!formData.name || !formData.phoneNumber) {
            alert("Please enter your full name and phone number");
            return false;
        } else if (!formData.email) {
            alert("Please enter your email");
            return false;
        } else if (!formData.password) {
            alert("Please enter your password");
            return false;
        }
        return true;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        if (validateForm()) {
            const post = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: formData.name,
                    phoneNumber: formData.phoneNumber,
                    email: formData.email,
                    password: formData.password,
                })
            };

            console.log('Posting data:', JSON.stringify(formData));

            fetch('http://127.0.0.1:5000/users', post)
                .then(response => {
                    if (!response.ok) {
                        alert("Email already exists or there was an error");
                        return response.json().then(err => { throw new Error(err.error) });
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Success:', data);
                    // Optionally, you can redirect or show a success message
                })
                .catch((error) => {
                    console.error('Error:', error);
                    setError(error.message); // Set the error message to state
                });
        }
    };

    return (
        <div className="signup-container">
            <form className="signup-form" onSubmit={handleSubmit}>
                <label>Firstname</label>
                <input type="text" placeholder="Firstname" onChange={handleOnChange} name="name" value={formData.name} />
                <label>Lastname</label>
                <input type="text" placeholder="Lastname" onChange={handleOnChange} name="phoneNumber" value={formData.phoneNumber} />
                <label>Email</label>
                <input type="email" placeholder="Email" onChange={handleOnChange} name="email" value={formData.email} />
                <label>Password</label>
                <input type="password" placeholder="Password" onChange={handleOnChange} name="password" value={formData.password} />
                <button type="submit">Sign Up</button>
            </form>
            {error && <p className="error-message">{error}</p>}
        </div>
    );
}

export default SignUp;
