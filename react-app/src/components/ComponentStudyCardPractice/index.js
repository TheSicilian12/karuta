import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { useParams, useHistory } from 'react-router-dom';

import OpenModalButton from "../OpenModalButton";
import OpenModalAddCardToDeck from "../OpenModalAddCardToDeck";
import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";

import { getDeckTHUNK } from "../../store/decks";

import "./ComponentStudyCardPractice.css";

export default function ComponentStudyCardPractice({cards, study}) {
  const dispatch = useDispatch();
  const history = useHistory();

  const [randNum, setRandNum] = useState(Math.floor(Math.random() * cards.length));
  const [showAnswer, setShowAnswer] = useState(false);
  const [showLongAnswer, setShowLongAnswer] = useState(false);


  const newCard = () => {
    setRandNum(Math.floor(Math.random() * cards.length));
    setShowAnswer(false);
    setShowLongAnswer(false);
  }

  // const [displayCard, setDisplayCard] = useState(cardsObj?.cards[0])

  return (
    <div>
      card
      <ComponentStudyCardQuestion cardData={cards[randNum]} deckId={""} study={study} />
      <button
        onClick={() => newCard()}>
        Next
      </button>
      <button
        onClick={() => setShowAnswer(!showAnswer)}>
        show answer
      </button>
      <button
        onClick={() => setShowLongAnswer(!showLongAnswer)}>
        show long answer
      </button>
      {showAnswer === true && <ComponentStudyCardAnswer cardData={cards[randNum]} deckId={""} study={study}/>}
      {showLongAnswer === true && <ComponentStudyCardAnswer cardData={cards[randNum]} deckId={""} longAnswer={true} study={study}/>}
    </div>
  );
}
