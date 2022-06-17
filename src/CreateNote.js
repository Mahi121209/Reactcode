import React from 'react';
import { Button } from '@material-ui/core';
import AddIcon from '@material-ui/icons/Add';


const CreateNote = (props) => {
    const [note, setNote] = React.useState({
        title:'',
        content: '',
    });

    const InputEvent = (event) => {
    // const value = event.target.value;
    // const name = event.target.name;

    const {name, value} = event.target;
        setNote((prevData) => {
            return {
                ...prevData,
                [name] :value,

            }
        })
    };

    const addEvent = ()  => {
    props.passNote(note);
    setNote({
        title:'',
        content: '',
    });
    };

    console.log("Note",note)

    return (
        <>
       <div style={{backgroundColor: 'red'}}>
        <form >
            <input type='text' name='title' placeholder="Title"  value={note.title} onChange={InputEvent} />
            <textarea name='content' value={note.content} onChange={InputEvent} rows="" column="" placeholder="write a note" style={{ position: 'relative', marginTop: '5%', backgroundColor: 'yellow'}}></textarea>
            <Button onClick={addEvent}>
           <AddIcon />
            </Button>
        </form>
       </div>
        </>
    )
};

export default CreateNote;