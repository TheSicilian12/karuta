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
  const [question, setQuestion] = useState(cardData.question);
  const [answer, setAnswer] = useState(cardData.answer);
  const [answerLong, setAnswerLong] = useState(cardData.answer_long);
  const [displayAnswer, setDisplayAnswer] = useState('short');
  const [additional, setAdditional] = useState(false);


  const { closeModal } = useModal();

  const handleSubmit = (e) => {
    e.preventDefault();
  }

  const handleAdditionalEdit = () => {
    setAdditional(true);
  }

  const displayAnswerTitle = (displayAsnwer, setDisplayAnswer) => {
    return (
      <>
        <div className="displayFlex open-modal-answers-title-container">
          <h2 className={displayAnswer === 'short' ? `open-modal-answer-${displayAnswer}-title-container` : ''}
            onClick={() => setDisplayAnswer('short')}>
            Edit Short Answer
          </h2>
          <h2 className={displayAnswer === 'long' ? `open-modal-answer-${displayAnswer}-title-container` : ''}
            onClick={() => setDisplayAnswer('long')}>
            Edit Long Answer
          </h2>
        </div>

        <textarea
          className="open-modal-edit-question-text-container"
          type="text"
          value={displayAnswer === 'short' ? answer : answerLong}
          onChange={(e) => {
            displayAnswer === 'short' ? setAnswer(e.target.value) : setAnswerLong(e.target.value)
            // setDisQuestionErr(true)
          }}
          placeholder="answer"
        >
        </textarea>
      </>
    )
  }

  // console.log("answer :", answer)
  // console.log("answerLong: ", answerLong)

  console.log("additional: ", additional)

  return (
    <div className="delete-comment-modal-container">
      <form
        onSubmit={handleSubmit}>

        {/* main edit*/}
        {editType === 'question' && <div>
          <h1>Edit Question</h1>
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
          {displayAnswerTitle(displayAnswer, setDisplayAnswer)}
        </div>}

        {additional === false && <button
          onClick={handleAdditionalEdit}>
          Would you like to edit the {editType === 'question' ? 'answer' : 'question'}
        </button>}

        {editType === 'question' && additional === true && <div>
          Answer
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
        {editType === 'answer' && additional === true && <div>
          Question
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




        <button
          type="submit">
          Save
        </button>
      </form>
    </div>
  );
}

export default OpenModalEditStudyCard;
