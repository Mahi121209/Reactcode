import React from "react";
import { FirstName, LastName } from "./App";

const ComC = () => {
  return (
    <>
      <FirstName.Consumer>
        {(fname) => {
          return (
          <LastName.Consumer>
            {(lastName) => {
              return (
                <h1>
                  My Name is {fname} {lastName}
                </h1>
              );
            }}
          </LastName.Consumer>
          )
        }}
      </FirstName.Consumer>
    </>
  );
};

export default ComC;
