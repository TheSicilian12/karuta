import React, { useEffect, useState } from "react";
import { useDispatch, useSelector} from 'react-redux';
import { useParams } from "react-router-dom";

import "./KarutaPoemPage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import ComponentPoem from "../ComponentPoem";
import LanguageToggle from "../LanguageToggle";
import {getOneKarutaCardTHUNK} from "../../store/karutaCards"

export default function KarutaPoemPage() {
  const dispatch = useDispatch();

  const [displayLanguage, setDisplayLanguage] = useState("english")

  const cardData = useSelector(state => state.karutaCards.singleCard)

  const {poemId} = useParams()

  useEffect(() => {
    dispatch(getOneKarutaCardTHUNK(poemId))
  }, [dispatch])

  if (!cardData) return null

  return (
    <div>
    Poem {poemId}
    <div>by: {cardData[poemId].author.english}</div>
    {/* <ComponentKarutaCard displayLanguage={displayLanguage} cardData={cardData[poemId]} size={'large'}/> */}
    <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"}/>
    <ComponentPoem language={displayLanguage} cardData={cardData[poemId]}/>
    </div>
  );
}
