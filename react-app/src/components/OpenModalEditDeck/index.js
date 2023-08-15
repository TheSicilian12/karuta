import React, { useState, useEffect } from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch, useSelector } from 'react-redux';

import './OpenModalEditDeck.css'
import '../UniversalCSS.css'

import { editDeckTHUNK, getDeckTHUNK } from '../../store/decks';
import { getCardsDivideTHUNK } from '../../store/studyCards';
import { getCardsDeckTHUNK } from "../../store/studyCards";

import ComponentStudyCardPreview from '../ComponentStudyCardPreview';

function OpenModalEditDeck({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className,
  deck
}) {
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);

  const { closeModal } = useModal();

  const [deckName, setDeckName] = useState(deck.name)

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("test")

    let payload = {
      deckId: deck.id,
      name: deckName,
      owner_id: deck.owner_id,
    }

    await dispatch(editDeckTHUNK(payload))
    if (deck.id) await dispatch(getDeckTHUNK(deck.id))
    closeModal();
  }

  return (
    <div>
      <form
        className="open-modal-edit-deck-form-container"
        onSubmit={handleSubmit}>

        <div className="open-modal-edit-deck-title-general">
          Change deck:
        </div>

        <div className="open-modal-edit-deck-title-name">
          {deck.name}
        </div>

        <input
          type="text"
          className="open-modal-edit-deck-input"
          value={deckName}
          onChange={(e) => {
            setDeckName(e.target.value)
          }}>
        </input>

        <button
          type="submit">
          Confirm edit
        </button>
      </form>

    </div>
  );
}

export default OpenModalEditDeck;
