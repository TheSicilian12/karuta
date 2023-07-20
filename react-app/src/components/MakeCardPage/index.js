import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from 'react-router-dom';

import "./MakeCardPage.css";

export default function MakeCardPage({ deckId }) {
  const dispatch = useDispatch();
  const history = useHistory();

  const [answer, setAnswer] = useState("");
  const [answerLong, setAnswerLong] = useState("");
  const [question, setQuestion] = useState("");

  const handleSubmit = (e) => {
    e.prevent.default()

    let payload = {
      question,
      answer,
      answerLong
    }

    if (deckId) payload.deckId = deckId
  }


  return (
    <div>
      Make Card Page

      <form
        onSubmit={handleSubmit}>

        <label>
          Question
        </label>
        <textarea
          className=''
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
          className=''
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
          className=''
          type='text'
          placeholder='long answer'
          value={answerLong}
          onChange={(e) => {
            setAnswerLong(e.target.value)
            // setDisplayAnswerLongErr(true)
          }}
        ></textarea>

          <button
            type='submit'>
            Make Card
          </button>
      </form>
    </div>
  );
}
