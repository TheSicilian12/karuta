import React, { useState } from "react";

import OpenModalButton from '../OpenModalButton';

import "./ComponentStudyCardPreview.css";
import "../UniversalCSS.css";


export default function ComponentStudyCardPreview({ cardData, deckId }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  // 2. deck id

  deckId = Number(deckId);

  let decks = cardData.decks;

  const addCard = () => {
    console.log("add card")

  }

  const removeCard = () => {
    console.log("remove card")
  }


  return (
    <div className="study-card-preview">
        <h2>
          {cardData.question}
        </h2>

        {!decks.includes(deckId) && <div
          onClick={() => addCard()}>
          <i className="fa fa-plus"></i>
        </div>}

        {decks.includes(deckId) && <div
          onClick={() => removeCard()}>
          <i className="fa fa-minus"></i>
        </div>}
    </div>
  );
}
