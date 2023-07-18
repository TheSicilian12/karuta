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
  // const [secondGuessCard, setSecondGuessCard] = useState("");


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

// need to take care of whether this is a "first" card or "second" card to send to the karuta card
// also need to take care of the randomization on this side.

  return (
    <div className="game-memory-container">
      Karuta Memory
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      <div>
        Test
        {Object.values(randomCards).map((card) => {
          return<div>
              <ComponentGameMemoryKarutaCard
                displayLanguage={displayLanguage}
                cardData={card}
                size={'small'}
                gameType={"matchHalf"}
                firstGuessCard={firstGuessCard}
                setFirstGuessCard={setFirstGuessCard}/>
            </div>
        })
        }
      </div>
    </div>
  );
}
