import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';

import { getCurrentUserDecksTHUNK } from "../../store/decks";
import { getCardsTHUNK } from "../../store/studyCards";

import "./StudyDeckPage.css";

export default function StudyDeckPage() {
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);
  const decks = useSelector(state => state.decks)
  const cards = useSelector(state => state.studyCards)

  console.log("decks: ", decks)
  useEffect(() => {
    dispatch(getCurrentUserDecksTHUNK(sessionUser.id));
    dispatch(getCardsTHUNK());
  }, [dispatch])

  if (Object.values(decks).length === 0) return <div>No decks</div>

  return (
    <div>
      StudyDeckPage
      {Object.values(decks).map((deck) => {
        return (
          <div>
            <NavLink to={`/studyDecks/${deck.id}`}>
              {deck.name}
            </NavLink>
          </div>
        )
      })}
      cards
      {Object.values(cards).map((card) => {
        return (
          <div>
            {/* <NavLink to={`/studyDecks/${deck.id}`}> */}
              {card.question}
            {/* </NavLink> */}
          </div>
        )
      })}

    </div>
  );
}
