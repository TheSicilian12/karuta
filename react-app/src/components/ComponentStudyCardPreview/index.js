import React, { useState } from "react";

import OpenModalButton from '../OpenModalButton';

import "./ComponentStudyCardPreview.css";
import "../UniversalCSS.css";

export default function ComponentStudyCardPreview({ cardData, deckId }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  deckId = Number(deckId);

  console.log("cardData: ", cardData.decks)
  let decks = cardData.decks;
  console.log("decks: ", decks)
  console.log("includes: ", decks.includes(deckId))

  return (
    <div className="study-card-preview">
        <h2>
          {cardData.question}
        </h2>

        {!decks.includes(deckId) && <button>
          <i className="fa fa-plus"></i>
        </button>}
        {decks.includes(deckId) && <button>
          <i className="fa fa-minus"></i>
        </button>}
    </div>
  );
}
