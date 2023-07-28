import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { useParams, useHistory } from 'react-router-dom';

import OpenModalButton from "../OpenModalButton";
import OpenModalAddCardToDeck from "../OpenModalAddCardToDeck";
import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";

import { getDeckTHUNK } from "../../store/decks";

import "./ComponentStudyCardPractice.css";

export default function ComponentStudyCardPractice({cards}) {
  const dispatch = useDispatch();
  const history = useHistory();

  const [randNum, setRandNum] = useState(Math.floor(Math.random() * cards.length))

  const newCard = () => {
    setRandNum(Math.floor(Math.random() * cards.length))
  }

  // const [displayCard, setDisplayCard] = useState(cardsObj?.cards[0])

  console.log("cards: ", cards)

  return (
    <div>
      card
      <ComponentStudyCardQuestion cardData={cards[randNum]} deckId={""} />
      <button
        onClick={() => newCard()}>
        Next
      </button>
    </div>
  );
}
