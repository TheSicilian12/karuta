import React, { useContext, useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getAllKarutaCardsTHUNK } from "../../store/karutaCards";

import "./HomePage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { Modal } from "../../context/Modal";

export default function HomePage() {
  const dispatch = useDispatch();
  const [displayLanguage, setDisplayLanguage] = useState("")

  const cards = useSelector(state => state.karutaCards)

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, [dispatch])

  if (!cards[1]) return null

  return (
   <div>
    Hello
    <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
    <ComponentKarutaCard language={displayLanguage} cardData={cards[1]} />
    </div>
  );
}
