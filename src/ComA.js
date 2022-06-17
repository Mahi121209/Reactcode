import React, { useEffect } from "react";
import axios from "axios";

const ComA = () => {
  const [num, setNum] = React.useState(3);

  useEffect(() => {
      async function getData() {
          const res = await axios.get(`https://pokeapi.co/api/v2/pokemon${num}`
          )
          console.log('res', res);
      }
      getData()
  });

  return (
    <>
    <h1> You choose {num} value</h1>
      <select
        value={num}
        onChange={(event) => {
          setNum(event.target.value);
        }}
        style={{ position: "relative", width: "10%" }}
      >
        <option value="1">1</option>
        <option value="25">25</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="6">6</option>
      </select>
    </>
  );
};

export default ComA;
