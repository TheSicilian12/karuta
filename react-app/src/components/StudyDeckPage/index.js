import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';

import { getCurrentUserDecksTHUNK } from "../../store/decks";
import { getCardsTHUNK } from "../../store/studyCards";

import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";

import "./StudyDeckPage.css";

export default function StudyDeckPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const sessionUser = useSelector(state => state.session.user);
  const decks = useSelector(state => state.decks)
  const cards = useSelector(state => state.studyCards)

  useEffect(() => {
    dispatch(getCurrentUserDecksTHUNK(sessionUser.id));
    dispatch(getCardsTHUNK());
  }, [dispatch])

  if (Object.values(decks).length === 0) return <div>No decks</div>

  const makeCard = () => {
    history.push(`/makeCard`)
  }

  const makeDeck = () => {
    history.push(`/makeDeck`)
  }

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
      <button
        onClick={makeCard}>
        <i className="fa fa-plus"></i> Make Card
      </button>
      <button
        onClick={makeDeck}>
        <i className="fa fa-plus"></i> Make Deck
      </button>
      {Object.values(cards).map((card) => {
        return (
          <div>
            {/* <NavLink to={`/studyDecks/${deck.id}`}> */}
              {card.question}
              <ComponentStudyCardQuestion cardData={card} deckId={""} />
              <ComponentStudyCardAnswer cardData={card} deckId={""}/>
            {/* </NavLink> */}
          </div>
        )
      })}

    </div>
  );
}
