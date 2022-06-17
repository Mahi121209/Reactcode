import React from 'react';
import Header from "./Header";


const Footer = () => {
    const year = new Date().getFullYear();
    return (
        <>
        <footer>
            <p> Copyright {year}</p>
        </footer>
        </>
    )
};

export default Footer;