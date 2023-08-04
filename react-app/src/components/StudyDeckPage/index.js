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

  const [display, setDisplay] = useState("decks")

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
    <div className="study-deck-page-container">
      <ComponentPageHeader title={"Your Study Page"} image={yourStudyPage}/>

    {/* <img src={yourStudyPage} /> */}

      {Object.values(decks).map((deck) => {
        return (
          <div>
            <NavLink className="study-deck-page-deck" to={`/studyDecks/${deck.id}`}>
              {/* <div className="study-deck-page-deck"> */}
                - {deck.name}
                {/* </div> */}
            </NavLink>
          </div>
        )
      })}

      <button
        onClick={makeDeck}>
        <i className="fa fa-plus"></i> Make a Deck
      </button>

      <button
        onClick={makeCard}>
        <i className="fa fa-plus"></i> Make a Card
      </button>

      {/* {Object.values(cards).map((card) => {
        return (
          <div>
              <ComponentStudyCardQuestion cardData={card} deckId={""} />
              <ComponentStudyCardAnswer cardData={card} deckId={""}/>

          </div>
        )
      })} */}

    </div>
  );
}
