import { useState } from "react"
import '../Styles/signup.css'

function SignUp() {
    const [formData, setFormData] = useState({
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        confirmPassword: ""
    })

    const [error, setError] = useState("")

    const handleOnChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
        setError("");
    }

    const validateForm=() =>{
        if (!formData.firstName || !formData.lastName) {
            alert("Please enter your full names");
            return false;
            } else if (!formData.email) {
                alert("Please enter your email");
                return false;   
        } else if (formData.password !== formData.confirmPassword) {
            alert("Passwords do not match")
            return false;
            }
        else {
            return true;
            }
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
                    firstName: formData.firstName,
                    lastName: formData.lastName,
                    email: formData.email,
                    password: formData.password,
                    status: "active"
                })
            };
            fetch('http://127.0.0.1:5000/user', post)
                .then(response => {
                    if (!response.ok) {
                        alert("Email already exists");
                        return response.json().then(err => { throw new Error(err.error) });
                        
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Success:', data);
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
            <input type="text" placeholder="Firstname"  onChange={handleOnChange} name="firstName" value={formData.firstName}/>
            <label>Lastname</label>
            <input type="text" placeholder="Lastname"  onChange={handleOnChange} name="lastName" value={formData.lastName}/> 
            <label>email</label>
            <input type="text" placeholder="Email"  onChange={handleOnChange} name="email" value={formData.email}/>
            <label>Password</label>
            <input type="text" placeholder="Password"  onChange={handleOnChange} name="password" value={formData.password}/>
            <label>Confirm Password</label>
            <input type="text" placeholder="Confirm Password"  onChange={handleOnChange} name="confirmPassword" value={formData.confirmPassword}/>
            <button type="submit" onClick={(e)=>alert(e.target.value)}>SignUp</button>
        </form>
    </div>
)
}

export default SignUp;