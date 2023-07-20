import React, { useState } from "react";

import "./ComponentStudyCardQuestion.css";
import "../UniversalCSS.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

export default function ComponentStudyCardQuestion({ cardData }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  console.log("study card")
  console.log("cardData: ", cardData)
  return (
    <div className="displayFlex">
        {cardData.question}
    </div>
  );
}
