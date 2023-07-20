import React, { useState } from "react";

import "./ComponentStudyCardAnswer.css";
import "../UniversalCSS.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

export default function ComponentStudyCardAnswer({ cardData }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  console.log("study card")
  console.log("cardData: ", cardData)
  return (
    <div className="study-card-answer-container">
        {cardData.answer}
    </div>
  );
}
