import React, { useEffect } from 'react';

const Statewise = () => {

    const getCovidData = async () => {
        const res = await fetch('https://api.covid19india.org/data.json');
        const actualData = await res.json();
        console.log(actualData);
    }

// console.log("Mahipal")

useEffect(() => {
getCovidData();
}, []);

    return (
        <>
        <h1> INDIA COVID-19 Dashboard</h1>
        </>
    )
};

export default Statewise;