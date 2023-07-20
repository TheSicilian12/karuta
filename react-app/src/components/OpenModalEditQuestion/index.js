import React, { useState } from 'react';
import { useModal } from '../../context/Modal';

import './OpenModalEditQuestion.css'
import '../UniversalCSS.css'

function OpenModalEditQuestion({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className,
  cardData
}) {
  const [question, setQuestion] = useState(cardData.question)

  const { closeModal } = useModal();
  console.log("cardData: ", cardData)
  return (
    <div className="delete-comment-modal-container">
      <h1>Q. {question}</h1>
      <div>
        <textarea
          type="text"
          value={question}
          onChange={(e) => {
            setQuestion(e.target.value)
            // setDisQuestionErr(true)
          }}
          placeholder="question"
        >
        </textarea>
      </div>
    </div>
  );
}

export default OpenModalEditQuestion;
