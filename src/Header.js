import React from "react";
import logo from './images/mmmJPG.JPG';
import Footer from "./Footer";

const Header = () => {
  return (
    <>
      <div style={{backgroundColor: 'blue'}}>
       <img src={logo}  alt="logo" width='10%' height='30%'/>
       
      </div>
    </>
  );
};

export default Header;
