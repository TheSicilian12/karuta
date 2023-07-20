import React, { useState } from "react";

import OpenModalButton from '../OpenModalButton';
import "./ComponentStudyCardQuestion.css";
import "../UniversalCSS.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";
import OpenModalEditStudyCard from "../OpenModalEditStudyCard";

export default function ComponentStudyCardQuestion({ cardData }) {
  // ComponentStudyCard takes in:
  // 1. study card data

  const handleEdit = () => {

  }

  return (
    <div className="study-card-question-container break-word">
        <h2>
          {cardData.question}
        </h2>

     <OpenModalButton
      className="study-card-question-edit-icon"
      buttonText={<i className="fa fa-pen"></i>}
      modalComponent={<OpenModalEditStudyCard cardData={cardData} editType={'question'}/>}/>
    </div>
  );
}
