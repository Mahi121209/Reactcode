import React from "react";
import { questions } from "./API";
import MyAccordion from './MyAccordion';

const Accordion = () => {
 const [data] = React.useState(questions);

  return (
    <>
    <section className='main_div'>
        <h1>React Interview question and answer</h1>
    {
    data.map((curElement) => {
    const { id, question, answer} = curElement;
   return <MyAccordion key={ id} {...curElement}/>
})}
    </section>
    </>
  );
};

export default Accordion;