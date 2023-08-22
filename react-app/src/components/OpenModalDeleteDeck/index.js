import React, { useState, useEffect } from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch, useSelector } from 'react-redux';

import './OpenModalDeleteDeck.css'
import '../UniversalCSS.css'

import { deleteDeckTHUNK, getDeckTHUNK } from '../../store/decks';

function OpenModalDeleteDeck({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className,
  cardData,
  editType,
  // deckId,
  deck
}) {
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);
  const cardsAll = useSelector(state => state.studyCards);

  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("delete button")
    dispatch(deleteDeckTHUNK(deck.id))

    closeModal();
  }

  return (
    <form
      className="modal-delete-deck-container"
      onSubmit={handleSubmit}>

    <div>
      <div className="open-modal-delete-deck-title-general">
        Delete
      </div>

      <div className="open-modal-delete-deck-title-name">
        {deck.name}
      </div>

    </div>
      <div>
        <button
          type='submit'>
          Yes, delete this deck
        </button>
        <button
          type="button"
          onClick={closeModal}>
          No
        </button>
      </div>

    </form>
  );
}

export default OpenModalDeleteDeck;
