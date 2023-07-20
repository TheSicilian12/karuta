import React, { useState } from "react";

import "./ComponentStudyCard.css";
import "../UniversalCSS.css";
import { NavLink } from "react-router-dom/cjs/react-router-dom.min";

export default function ComponentStudyCard({ cardData }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  console.log("study card")
  console.log("cardData: ", cardData)
  return (
    <div className="displayFlex">
        Study card
    </div>
  );
}
