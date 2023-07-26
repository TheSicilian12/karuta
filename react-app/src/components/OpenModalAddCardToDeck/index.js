import React, { useState, useEffect } from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch, useSelector } from 'react-redux';

import './OpenModalAddCardToDeck.css'
import '../UniversalCSS.css'

import { getDeckTHUNK } from '../../store/decks';
import { getCardsTHUNK } from '../../store/studyCards';

function OpenModalAddCardToDeck({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className,
  cardData,
  editType,
  deckId
}) {
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);
  const cards = useSelector(state => state.studyCards);

  const { closeModal } = useModal();

  useEffect(() => {
    dispatch(getCardsTHUNK());
  }, [dispatch])

  if (!cards) return null;

  const handleSubmit = async (e) => {
    e.preventDefault();


    closeModal();
  }

  return (
    <div className="open-modal-add-card-to-deck">
      <form
        onSubmit={handleSubmit}>
        test
        {Object.values(cards).map(card => {
          return (
            <div>
              {card.question}
            </div>
          )
        })}

      </form>
    </div>
  );
}

export default OpenModalAddCardToDeck;
