import React, { useState } from "react";
import { useDispatch } from "react-redux";

import OpenModalButton from '../OpenModalButton';

import "./ComponentStudyCardPreview.css";
import "../UniversalCSS.css";
import { associateCardDeckTHUNK, disassociateCardDeckTHUNK, getCardsDivideTHUNK, testTHUNK } from "../../store/studyCards";


export default function ComponentStudyCardPreview({ cardData, deckId }) {
  // ComponentStudyCard takes in:
  // 1. study card data
  // 2. deck id
  const dispatch = useDispatch();

  deckId = Number(deckId);

  let decks = cardData.decks;

  const addCard = async () => {
    console.log("add card")
    await dispatch(associateCardDeckTHUNK(cardData, deckId));
    await dispatch(getCardsDivideTHUNK(deckId));
  }

  const removeCard = async () => {
    console.log("remove card")
    await dispatch(disassociateCardDeckTHUNK(cardData.id, deckId));
    await dispatch(getCardsDivideTHUNK(deckId));
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
