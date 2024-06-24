import React from 'react'
import { Link , useNavigate} from 'react-router-dom'
// import '../Styles/NavBar.css'

const NavBar = ({email}) => {

    const navigate = useNavigate()

    function handleLogout(){
        localStorage.removeItem("access_token")
        navigate("/login")

    }

    
    return (
        <nav className='navbar' >
            <div className='container'>
                <div className='logo' >
                Green Carbon Tracker
                </div>
                <div className='menu'>
                    <ul>
                        <li>
                            <Link to='/'>HomePage</Link>
                        </li>
                        <li>
                            <Link to='/login'> Login</Link>
                        </li>
                        <li>
                            <Link to='/signup'> SignUp</Link>
                        </li>                      
                        
                        <li>
                            <button onClick={handleLogout} className="logout" >Logout</button>
                        </li>
                        <li>({email})</li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}

export default NavBar