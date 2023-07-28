import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { useParams, useHistory } from 'react-router-dom';

import OpenModalButton from "../OpenModalButton";
import OpenModalAddCardToDeck from "../OpenModalAddCardToDeck";
import OpenModalDeleteDeck from "../OpenModalDeleteDeck";
import ComponentStudyCardQuestion from "../ComponentStudyCardQuestion";
import ComponentStudyCardAnswer from "../ComponentStudyCardAnswer";

import { getDeckTHUNK } from "../../store/decks";

import "./DeckPage.css";

export default function DeckPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const { deckId } = useParams()

  const [displayLanguage, setDisplayLanguage] = useState("english")

  // const sessionUser = useSelector(state => state.session.user);
  const cardsObj = useSelector(state => state.decks.singleDeck)
  // console.log("decks: ", decks)
  useEffect(() => {
    dispatch(getDeckTHUNK(deckId))
  }, [dispatch])

  if (!cardsObj) return <div>No cards object</div>
  const cards = cardsObj.cards

  const makeCard = () => {
    history.push(`/makeCard/${deckId}`)
  }

  const studyDeck = () => {
    history.push(`/study/${deckId}`)
  }

  return (
    <div>
      DeckPage
      <button
        onClick={makeCard}>
        <i className="fa fa-plus"></i> Make Card
      </button>

    <div>
      <OpenModalButton
      className="study-card-question-edit-icon"
      buttonText={<i className="fa fa-plus"></i>}
      modalComponent={<OpenModalAddCardToDeck deckId={deckId}/>}/>
    </div>
    <div>
      <OpenModalButton
      className="study-card-question-edit-icon"
      buttonText={<i className="fa fa-minus">Delete</i>}
      modalComponent={<OpenModalDeleteDeck deckId={deckId}/>}/>
    </div>

      {cardsObj?.cards[0] ? <button
        onClick={studyDeck}>
        Study Deck
      </button> :
      <div>
        This deck has no cards
        </div>}

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
