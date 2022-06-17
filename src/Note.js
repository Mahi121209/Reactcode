import React from "react";
import { Button } from "@material-ui/core";
import DeleteIcon from "@material-ui/icons/Delete";

const Note = () => {
  const deleteNote = () => {
    props.DeleteIcon(props.id);
  };
  return (
    <>
      <div>
        <h1> Titel </h1>
        <br />
        <p> This is the content </p>
        <Button onClick={deleteNote}>
          <DeleteIcon />
        </Button>
      </div>
    </>
  );
};

export default Note;
