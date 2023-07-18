import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import "./GameKarutaMemory.css";
import ComponentGameMemoryKarutaCard from "../ComponentGameMemoryKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { getRandomKarutaCardsTHUNK } from "../../store/karutaCards";

export default function GameKarutaMemory({ gameSize }) {
  const dispatch = useDispatch();
  const [displayLanguage, setDisplayLanguage] = useState("english")
  const [firstGuessCard, setFirstGuessCard] = useState("");
  const [secondGuessCard, setSecondGuessCard] = useState("");


  const randomCards = useSelector(state => state.karutaCards)

  // retreive a random set of cards depending on the game size
  useEffect(() => {
    dispatch(getRandomKarutaCardsTHUNK(gameSize))
  }, [dispatch])

  if (Object.keys(randomCards).length === 0) return null

  console.log("randomCards: ", randomCards)
  Object.values(randomCards).forEach((card) => {
    console.log("card: ", card)
  })

  return (
    <div className="game-memory-container">
      Karuta Memory
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      <div>
        Test
        {Object.values(randomCards).map((card) => {
          return<div>
              <ComponentGameMemoryKarutaCard displayLanguage={displayLanguage} cardData={card} size={'small'} gameType={"second"}/>
            </div>
        })
        }
      </div>
    </div>
  );
}
