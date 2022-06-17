import React from 'react';
import axios, { Axios } from 'axios';



const Post = () => {
const url = "";
const [data, setData] = React.useState({
    name: "",
    date: "",
    iduser: ""
});

const Submit = (e) => {
 e.preventDefault();
 Axios.post(url,{
     name:data.name,
     date: data.date,
     iduser:data.iduser
 })
 .then(res => {
     console.log(res.data);
 })
};

function handle(e){
 const newdata = {...data};
 newdata[e.target.id] = e.target.value
 setData(newdata);
 console.log(newdata);
}
    return (
        <>
        <form onSubmit={(e)=> Submit(e)}>
            <input onChange={(e) =>handle(e)} id="name" value={data.name} placeholder='name' type="text"></input>
            <input  onChange={(e) =>handle(e)} id="date" value={data.date} placeholder='date' type="date"></input>
            <input  onChange={(e) =>handle(e)} id="iduser" value={data.iduser} placeholder='iduser' type="number"></input>
        <button >Submit</button>
        </form>
        </>
    )
}

export default Post;