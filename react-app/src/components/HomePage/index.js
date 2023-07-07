import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getAllKarutaCardsTHUNK } from "../../store/karutaCards";

import "./HomePage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";

export default function HomePage() {
  const dispatch = useDispatch();

  const cards = useSelector(state => state.karutaCards)
  console.log("cards: ", cards)

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, [dispatch])

  // console.log("card: ", cards[1].author)

  if (!cards[1]) return null

  return (
   <div>
    Hello
    <ComponentKarutaCard cardData={cards[1]} />
    </div>
  );
}
