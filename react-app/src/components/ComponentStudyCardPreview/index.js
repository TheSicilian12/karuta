import React, { useState } from "react";

import OpenModalButton from '../OpenModalButton';

import "./ComponentStudyCardPreview.css";
import "../UniversalCSS.css";

export default function ComponentStudyCardPreview({ cardData }) {
  // ComponentStudyCard takes in:
  // 1. study card data

  return (
    <div className="study-card-preview">
        <h2>
          {cardData.question}
        </h2>
        
        <button>
          <i className="fa fa-plus"></i>
        </button>
        <button>
          <i className="fa fa-minus"></i>
        </button>
    </div>
  );
}
