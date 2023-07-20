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

  return (
    <div>
      Make Card Page

      <form>

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


      </form>
    </div>
  );
}
