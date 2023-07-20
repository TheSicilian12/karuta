import React, { useState } from "react";

import OpenModalButton from '../OpenModalButton';
import "./ComponentStudyCardAnswer.css";
import "../UniversalCSS.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import OpenModalEditStudyCard from "../OpenModalEditStudyCard";

export default function ComponentStudyCardAnswer({ cardData, deckId }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  console.log("study card")
  console.log("cardData: ", cardData)
  return (
    <div className="study-card-answer-container">
        {cardData.answer}

        <OpenModalButton
      className="study-card-question-edit-icon"
      buttonText={<i className="fa fa-pen"></i>}
      modalComponent={<OpenModalEditStudyCard cardData={cardData} editType={'answer'} deckId={deckId}/>}/>
    </div>
  );
}
