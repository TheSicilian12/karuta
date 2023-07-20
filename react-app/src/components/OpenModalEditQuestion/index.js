import React from 'react';
import { useModal } from '../../context/Modal';

import './OpenModalEditQuestion.css'
import '../UniversalCSS.css'

function OpenModalEditQuestion({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className
}) {
  const { closeModal } = useModal();

  return (
      <div className="delete-comment-modal-container">
          Hello
      </div>
  );
}

export default OpenModalEditQuestion;
