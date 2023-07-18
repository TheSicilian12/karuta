import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { shuffleObj } from "../ComponentFunctions";

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
  let randomCardsDouble = {}

  // determine which cards should show the first part of the card or the second part
  Object.values(randomCards).map((card) => {
    randomCardsDouble[card.id] = { ...card, 'match': 'first' }
    randomCardsDouble[card.id + 100] = { ...card, 'match': 'second' }
  })

  let randomCardsArr = shuffleObj(randomCardsDouble)

  return (
    <div className="game-memory-container">
      Karuta Memory
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      <div>
        Test
        {randomCardsArr.map((card) => {
          return <div>
            <ComponentGameMemoryKarutaCard
              displayLanguage={displayLanguage}
              cardData={card}
              size={'small'}
              gameType={"matchHalf"}
              firstGuessCard={firstGuessCard}
              setFirstGuessCard={setFirstGuessCard} />
          </div>
        })
        }
      </div>
    </div>
  );
}
