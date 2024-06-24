// HomePage.js
import { useContext } from "react";
import { UserContext } from "./UserContext";
import Contact from "./Contact";
import FAQ from "./FAQ";
import Landing from "./Landing";
import Page1 from "./page1";
import Page2 from "./page2";
import Page3 from "./page3";
import Page4 from "./page4";
import Page5 from "./page5";

function HomePage() {
    const { user } = useContext(UserContext);

    return (
        <>
            {user && <span>Welcome {user.name}, {user.email}</span>}
            <Landing />
            <Page1 />
            <Page2 />
            <Page4 />
            <Page5 />
            <FAQ />
            <Contact />
             
        </>
    );
}

export default HomePage;
