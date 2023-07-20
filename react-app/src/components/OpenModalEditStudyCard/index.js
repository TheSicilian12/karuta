import React, { useState } from 'react';
import { useModal } from '../../context/Modal';

import './OpenModalEditStudyCard.css'
import '../UniversalCSS.css'

function OpenModalEditStudyCard({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className,
  cardData,
  editType
}) {
  const [question, setQuestion] = useState(cardData.question)
  const [answer, setAnswer] = useState(cardData.answer)
  const [answerLong, setAnswerLong] = useState(cardData.answer_long)



  const { closeModal } = useModal();

  const handleSubmit = (e) => {
    e.preventDefault();
  }

  console.log("cardData: ", cardData)

  return (
    <div className="delete-comment-modal-container">
      <form
        onSubmit={handleSubmit}>

      {editType === 'question' && <h1>Edit Question</h1>}
      {editType === 'answer' && <h1>Edit Answer</h1>}

      {/* main edit*/}
      {editType === 'question' && <div>
        <textarea
          className="open-modal-edit-question-text-container"
          type="text"
          value={question}
          onChange={(e) => {
            setQuestion(e.target.value)
            // setDisQuestionErr(true)
          }}
          placeholder="question"
        >
        </textarea>
      </div>}
      {editType === 'answer' && <div>
        <textarea
          className="open-modal-edit-question-text-container"
          type="text"
          value={answer}
          onChange={(e) => {
            setAnswer(e.target.value)
            // setDisQuestionErr(true)
          }}
          placeholder="question"
        >
        </textarea>


      </div>}






      <button
        type="submit">
          Save
      </button>
      </form>
    </div>
  );
}

export default OpenModalEditStudyCard;
