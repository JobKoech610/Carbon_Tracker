import { useState } from "react";


function LogIn() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);


    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch('http://127.0.0.1:5000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email, password }),
            });
            const data = await response.json();
            if (data.token) {
                localStorage.setItem('token', data.token);
                console.log("Name:", data.name);
                console.log("Email:", data.email);
                console.log("Welcome")
            } else {
                setError(data.message || "Login failed");
            }
        } catch (error) {
            setError('An error occurred, please try again');
        }
    };

    return (
        <div>
            <form onSubmit={handleLogin}>
                <label>Email</label>
                <input
                    type="text"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <br />
                <label>Password</label>
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br />
                <button type="submit">Login</button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>} {/* Display error message */}
        </div>
    );
}

export default LogIn;
