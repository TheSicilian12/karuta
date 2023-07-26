import React, { useState } from "react";

import OpenModalButton from '../OpenModalButton';

import "./ComponentStudyCardPreview.css";
import "../UniversalCSS.css";

export default function ComponentStudyCardPreview({ cardData }) {
  // ComponentStudyCard takes in:
  // 1. study card data

  return (
    <div className="">
        <h2>
          {cardData.question}
        </h2>
    </div>
  );
}
