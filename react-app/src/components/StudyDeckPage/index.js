import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';

import yourStudyPage from "../../resources/images/yourStudyPage.jpg";

import { getCurrentUserDecksTHUNK } from "../../store/decks";
import { getCardsTHUNK } from "../../store/studyCards";

import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";

import "./StudyDeckPage.css";
import ComponentPageHeader from "../ComponentPageHeader";

export default function StudyDeckPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const sessionUser = useSelector(state => state.session.user);
  const decks = useSelector(state => state.decks)
  const cards = useSelector(state => state.studyCards)

  const [displayCSS, setDisplayCSS] = useState("study-deck-page-toggle-selected")
  const [displaySelection, setDisplaySelection] = useState(true);

  useEffect(() => {
    if (sessionUser) dispatch(getCurrentUserDecksTHUNK(sessionUser.id));
    dispatch(getCardsTHUNK());
  }, [dispatch])

  if (!sessionUser) return <div>Please sign in</div>
  if (Object.values(decks).length === 0) return <div>No decks</div>

  const makeCard = () => {
    history.push(`/makeCard`)
  }

  const makeDeck = () => {
    history.push(`/makeDeck`)
  }

  return (
    <div className="study-deck-page-container">
      <ComponentPageHeader title={"Your Study Page"} image={yourStudyPage} />

      <div className="study-deck-page-toggle-container">
        <div className={displaySelection ? `${displayCSS} study-deck-page-cardDeck-buttons`
          : "study-deck-page-toggle-notSelected study-deck-page-cardDeck-buttons"}
          onClick={() => setDisplaySelection(true)}>
          Decks</div>
        <div className={!displaySelection ? `${displayCSS} study-deck-page-cardDeck-buttons`
          : "study-deck-page-toggle-notSelected study-deck-page-cardDeck-buttons"}
          onClick={() => setDisplaySelection(false)}>
          Cards</div>
      </div>

      {displaySelection && <h1>Your Decks</h1>}
      {!displaySelection && <h1>Your Cards</h1>}

      {displaySelection && <button
        className="button-basic"
        onClick={makeDeck}>
        <i className="fa fa-plus"></i> New Deck
      </button>}

      {!displaySelection && <button
        className="button-basic"
        onClick={makeCard}>
        <i className="fa fa-plus"></i> New Card
      </button>}

      {displaySelection && <div className="study-deck-page-deck-container">
        {Object.values(decks).map((deck) => {
          return (
            <NavLink className="study-deck-page-deck-navLink" to={`/studyDecks/${deck.id}`}>
              <div className="study-deck-page-deck">
                {deck.name}
              </div>
            </NavLink>
          )
        })}
      </div>}

      {!displaySelection && Object.values(cards).map((card) => {
        return (
          <div className="study-deck-page-cards-container">
              <ComponentStudyCardQuestion cardData={card} deckId={""} />
          </div>
        )
      })}

    </div>
  );
}
