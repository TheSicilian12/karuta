import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from 'react-router-dom';

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
      Make Deck Page

      <form
        onSubmit={handleSubmit}>

        <label>
          Deck Name
        </label>
        <textarea
          className=''
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
