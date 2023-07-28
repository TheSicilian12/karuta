import React, { useState } from "react";

import OpenModalButton from '../OpenModalButton';
import "./ComponentStudyCardAnswer.css";
import "../UniversalCSS.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import OpenModalEditStudyCard from "../OpenModalEditStudyCard";

export default function ComponentStudyCardAnswer({ cardData, deckId, longAnswer}) {
  // ComponentStudyCard takes in:
  // 1. study card data
  console.log("longAnswer: ", typeof longAnswer)
  return (
    <div className="study-card-answer-container">
        {cardData.answer}
        {longAnswer === true && <div>{cardData.answer_long}</div>}
        <OpenModalButton
      className="study-card-question-edit-icon"
      buttonText={<i className="fa fa-pen"></i>}
      modalComponent={<OpenModalEditStudyCard cardData={cardData} editType={'answer'} deckId={deckId}/>}/>
    </div>
  );
}
