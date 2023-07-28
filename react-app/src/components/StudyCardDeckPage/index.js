import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { useParams, useHistory } from 'react-router-dom';

import OpenModalButton from "../OpenModalButton";
import OpenModalAddCardToDeck from "../OpenModalAddCardToDeck";
import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";
import ComponentStudyCardPractice from "../ComponentStudyCardPractice";

import { getDeckTHUNK } from "../../store/decks";

import "./StudyCardDeckPage.css";

export default function StudyCardDeckPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const { deckId } = useParams()

  // const sessionUser = useSelector(state => state.session.user);
  const cardsObj = useSelector(state => state.decks.singleDeck)

  const [displayCard, setDisplayCard] = useState(cardsObj?.cards[0])

  useEffect(() => {
    dispatch(getDeckTHUNK(deckId))
  }, [dispatch])

  if (!cardsObj) return <div>No cards</div>
  // if (!cardsObj.cards[0]) return <div>No cards</div>
  const cards = cardsObj.cards


  console.log("cardsObj: ", cardsObj.cards)
  console.log("displayCard: ", displayCard)

  return (
    <div>
      Study cards
      <ComponentStudyCardPractice cards={cardsObj.cards}/>

    </div>
  );
}
