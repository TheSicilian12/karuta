import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from 'react-router-dom';

import MakeCardPage from ".";

import "./MakeCardPage.css";

export default function MakeCardPageWrapper() {
  const dispatch = useDispatch();
  const history = useHistory();

  const { deckId } = useParams()



  return (
    <div>
      <MakeCardPage deckId={deckId}/>
    </div>
  );
}
