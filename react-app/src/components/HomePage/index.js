import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getAllKarutaCardsTHUNK } from "../../store/karutaCards";

import "./HomePage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";

export default function HomePage() {
  const dispatch = useDispatch();

  const cards = useSelector(state => state.karutaCards)

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, [dispatch])


  return (
   <div>
    Hello
    <ComponentKarutaCard cardData={cards[0]}/>
    </div>
  );
}
