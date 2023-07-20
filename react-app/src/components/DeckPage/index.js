import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams } from 'react-router-dom';

import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";

import { getCurrentUserDecksTHUNK, getDeckTHUNK } from "../../store/decks";

import "./DeckPage.css";

export default function DeckPage() {
  const dispatch = useDispatch();

  const { deckId } = useParams()

  const [displayLanguage, setDisplayLanguage] = useState("english")


  // const sessionUser = useSelector(state => state.session.user);
  const cardsObj = useSelector(state => state.decks.singleDeck)
  // console.log("decks: ", decks)
  useEffect(() => {
    dispatch(getDeckTHUNK(deckId))
  }, [dispatch])

  if (!cardsObj) return <div>No cards</div>
  const cards = cardsObj.cards

  return (
    <div>
      DeckPage
      <div>
        Cards
        {
          cards.map((card) => {
            return (
              <div className="displayFlex">
                <ComponentStudyCardQuestion cardData={card} deckId={deckId} />
                <ComponentStudyCardAnswer cardData={card} deckId={deckId}/>
              </div>
            )
          })
        }

      </div>
    </div>
  );
}
