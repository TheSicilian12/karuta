import React, { useEffect } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getAllKarutaCardsTHUNK } from "../../store/karutaCards";

import "./HomePage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { Modal } from "../../context/Modal";

export default function HomePage() {
  const dispatch = useDispatch();

  const cards = useSelector(state => state.karutaCards)

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, [dispatch])

  if (!cards[1]) return null

  return (
   <div>
    Hello
    
    <LanguageToggle languageOne={"english"} languageTwo={"japanese"} />
    <ComponentKarutaCard cardData={cards[1]} />
    </div>
  );
}
