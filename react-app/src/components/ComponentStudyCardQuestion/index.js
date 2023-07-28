import React, { useState } from "react";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

import OpenModalButton from '../OpenModalButton';
import OpenModalEditStudyCard from "../OpenModalEditStudyCard";
import OpenModalDeleteStudyCard from "../OpenModalDeleteStudyCard";

import "./ComponentStudyCardQuestion.css";
import "../UniversalCSS.css";

export default function ComponentStudyCardQuestion({ cardData, deckId }) {
  // ComponentStudyCard takes in:
  // 1. study card data

  return (
    <div className="study-card-question-container break-word">
      <h2>
        {cardData.question}
      </h2>

      <OpenModalButton
        className="study-card-question-edit-icon"
        buttonText={<i className="fa fa-pen"></i>}
        modalComponent={<OpenModalEditStudyCard cardData={cardData} editType={'question'} deckId={deckId} />} />

      <OpenModalButton
        className="study-card-question-edit-icon"
        buttonText={"Delete study card"}
        modalComponent={<OpenModalDeleteStudyCard cardId={cardData.id} />} />
    </div>
  );
}
