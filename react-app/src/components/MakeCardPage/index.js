import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from 'react-router-dom';

import deckPage from "../../resources/images/deckPage.jpg";

import ComponentPageHeader from "../ComponentPageHeader";

import "./MakeCardPage.css";
import { addCardTHUNK } from "../../store/studyCards";

export default function MakeCardPage({ deckId }) {
  const dispatch = useDispatch();
  const history = useHistory();

  const sessionUser = useSelector(state => state.session.user);

  const [answer, setAnswer] = useState("");
  const [answerLong, setAnswerLong] = useState("");
  const [question, setQuestion] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault()

    let payload = {
      question,
      answer,
      answerLong,
      ownerId: sessionUser.id
    }

    if (deckId) payload.deckId = deckId;

    setAnswer("");
    setAnswerLong("");
    setQuestion("");
  }


  return (
    <div>
       <ComponentPageHeader title={`Make Card`} image={deckPage} />

      <form
        className="make-card-page-container"
        onSubmit={handleSubmit}>

        <label>
          Question
        </label>
        <textarea
          className='make-card-page-input-question-container'
          type='text'
          placeholder='question'
          value={question}
          onChange={(e) => {
            setQuestion(e.target.value)
            // setDisplayQuestionErr(true)
          }}
        ></textarea>

        <label>
          Answer
        </label>
        <textarea
          className='make-card-page-input-answer-container'
          type='text'
          placeholder='answer'
          value={answer}
          onChange={(e) => {
            setAnswer(e.target.value)
            // setDisplayAnswerErr(true)
          }}
        ></textarea>

        <label>
          Long answer
        </label>
        <textarea
          className='make-card-page-input-answer-container'
          type='text'
          placeholder='long answer'
          value={answerLong}
          onChange={(e) => {
            setAnswerLong(e.target.value)
            // setDisplayAnswerLongErr(true)
          }}
        ></textarea>

          <button
            className="button-basic"
            type='submit'>
            Make Card
          </button>
      </form>
    </div>
  );
}
