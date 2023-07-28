import React, { useState, useEffect } from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch, useSelector } from 'react-redux';

import './OpenModalDeleteStudyCard.css'
import '../UniversalCSS.css'

import { deleteDeckTHUNK, getDeckTHUNK } from '../../store/decks';
import { deleteCardTHUNK } from '../../store/studyCards';

function OpenModalDeleteStudyCard({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className,
  cardData,
  editType,
  cardId
}) {
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);
  const cardsAll = useSelector(state => state.studyCards);
  const deck = useSelector(state => state.decks)

  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("delete button")
    dispatch(deleteCardTHUNK(cardId))

    closeModal();
  }

  return (
      <form
        onSubmit={handleSubmit}>

        <div>
          Delete
          Are you sure?
        </div>
        <button
          type='submit'>
          Yes, delete this study card
        </button>
        <button>
          No
        </button>


      </form>
  );
}

export default OpenModalDeleteStudyCard;
