import React, { useState } from "react";
import { useDispatch } from "react-redux";

import OpenModalButton from '../OpenModalButton';

import "./ComponentStudyCardPreview.css";
import "../UniversalCSS.css";
import { associateCardDeckTHUNK, disassociateCardDeckTHUNK, testTHUNK } from "../../store/studyCards";


export default function ComponentStudyCardPreview({ cardData, deckId }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  // 2. deck id
  const dispatch = useDispatch();

  deckId = Number(deckId);

  let decks = cardData.decks;

  const addCard = () => {
    console.log("add card")
    dispatch(associateCardDeckTHUNK(cardData, deckId))
  }

  const removeCard = () => {
    console.log("remove card")
    dispatch(disassociateCardDeckTHUNK(cardData.id, deckId))
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