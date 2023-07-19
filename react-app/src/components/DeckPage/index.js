import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams } from 'react-router-dom';

import { getCurrentUserDecksTHUNK, getDeckTHUNK } from "../../store/decks";

import "./DeckPage.css";

export default function DeckPage() {
  const dispatch = useDispatch();

  const {deckId} = useParams()

  // const sessionUser = useSelector(state => state.session.user);
  // const decks = useSelector(state => state.decks)

  // console.log("decks: ", decks)
  useEffect(() => {
    dispatch(getDeckTHUNK(deckId))
  }, [dispatch])

  // if (Object.values(decks).length === 0) return <div>No decks</div>

  return (
    <div>
      DeckPage
    </div>
  );
}
