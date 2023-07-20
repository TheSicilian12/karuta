import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams } from 'react-router-dom';

import ComponentKarutaCard from '../ComponentKarutaCard';
import { getCurrentUserDecksTHUNK, getDeckTHUNK } from "../../store/decks";

import "./DeckPage.css";

export default function DeckPage() {
  const dispatch = useDispatch();

  const {deckId} = useParams()

  const [displayLanguage, setDisplayLanguage] = useState("english")


  // const sessionUser = useSelector(state => state.session.user);
  const cardsObj = useSelector(state => state.decks.singleDeck)
  // console.log("decks: ", decks)
  useEffect(() => {
    dispatch(getDeckTHUNK(deckId))
  }, [dispatch])

  if (!cardsObj) return <div>No cards</div>
  const cards = cardsObj.cards
  cards.map((card) => {
    console.log("card: ", card)
  })

  return (
    <div>
      DeckPage
      <div>
        Cards
        

      </div>
    </div>
  );
}
