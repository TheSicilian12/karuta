import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { useParams, useHistory } from 'react-router-dom';

import deckPage from "../../resources/images/deckPage.jpg";

import OpenModalButton from "../OpenModalButton";
import OpenModalAddCardToDeck from "../OpenModalAddCardToDeck";
import OpenModalDeleteDeck from "../OpenModalDeleteDeck";
import OpenModalEditDeck from "../OpenModalEditDeck";
import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";

import { getDeckTHUNK } from "../../store/decks";
import { getCardsDeckTHUNK, getCardsDivideTHUNK } from "../../store/studyCards";
import ComponentPageHeader from "../ComponentPageHeader";


import "./DeckPage.css";

export default function DeckPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const { deckId } = useParams()

  const [displayLanguage, setDisplayLanguage] = useState("english")

  // const sessionUser = useSelector(state => state.session.user);
  const deck = useSelector(state => state.decks.singleDeck?.deck)
  const cardsObj = useSelector(state => state.studyCards)
  console.log("deck: ", deck)

  useEffect(() => {
    dispatch(getDeckTHUNK(deckId))
    // dispatch(getCardsDeckTHUNK(deckId))
    dispatch(getCardsDivideTHUNK(deckId));
  }, [dispatch])

  if (!cardsObj) return <div>No cards object</div>
  if (!cardsObj.inDeck) return <div>This deck has no cards</div>
  if (!deck) return <div>No deck</div>
  const cards = cardsObj.inDeck

  console.log("cards: ", cards)

  const makeCard = () => {
    history.push(`/makeCard/${deckId}`)
  }

  const studyDeck = () => {
    history.push(`/study/${deckId}`)
  }

  return (
    <div className="deck-page-container">
      <ComponentPageHeader title={`Deck: ${deck.name}`} image={deckPage} />

      <div className="">

        <div className="deck-page-title-container">

          <div className="deck-page-title">
            {deck.name}


            <div className="deck-page-deck-edit-buttons-container">
              <div>
                <OpenModalButton
                  className="study-card-question-edit-icon deck-page-medit-buttons-margin"
                  buttonText={<i className="fa fa-pen"></i>}
                  modalComponent={<OpenModalEditDeck deck={deck} />} />
              </div>

              <div>
                <OpenModalButton
                  className="study-card-question-edit-icon deck-page-medit-buttons-margin"
                  buttonText={<i className="fa fa-trash"></i>}
                  modalComponent={<OpenModalDeleteDeck deckId={deckId} />} />
              </div>
            </div>
          </div>
        </div>

      </div>

      <button
        onClick={makeCard}>
        <i className="fa fa-plus"></i> Make Card
      </button>

      <div>
        <OpenModalButton
          className="study-card-question-edit-icon"
          buttonText={<i className="fa fa-plus"></i>}
          modalComponent={<OpenModalAddCardToDeck deckId={deckId} />} />
      </div>

      {Object.values(cards).length !== 0 ? <button
        onClick={studyDeck}>
        Study Deck
      </button> :
        <div>
          This deck has no cards
        </div>}

      <div>
        Cards
        {
          Object.values(cards).map((card) => {
            return (
              <div className="displayFlex">
                <ComponentStudyCardQuestion cardData={card} deckId={deckId} />
                <ComponentStudyCardAnswer cardData={card} deckId={deckId} />
              </div>
            )
          })
        }

      </div>
    </div>
  );
}
