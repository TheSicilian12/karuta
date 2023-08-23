import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from 'react-router-dom';

import deckPage from "../../resources/images/deckPage.jpg";

import ComponentPageHeader from "../ComponentPageHeader";

import "./MakeDeckPage.css";
import { addDeckTHUNK } from "../../store/decks";

export default function MakeDeckPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const sessionUser = useSelector(state => state.session.user);

  const [deckName, setDeckName] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault()

    let payload = {
      name: deckName,
      owner_id: sessionUser.id
    }
    console.log("payload: ", payload)
    console.log("handleSubmit")
    dispatch(addDeckTHUNK(payload));
  }


  return (
    <div>
    <ComponentPageHeader title={`Make Deck`} image={deckPage} />

      <form
        className="make-deck-page-container"
        onSubmit={handleSubmit}>

        <h1>
          Deck Name
        </h1>
        <textarea
          className='make-deck-page-input-container'
          type='text'
          placeholder='deck name'
          value={deckName}
          onChange={(e) => {
            setDeckName(e.target.value)
            // setDisplayQuestionErr(true)
          }}
        ></textarea>

          <button
            type='submit'>
            Make Deck
          </button>
      </form>
    </div>
  );
}
