import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { shuffleObj } from "../ComponentFunctions";

import "./GameKarutaMemory.css";
import ComponentGameMemoryKarutaCard from "../ComponentGameMemoryKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { getRandomKarutaCardsTHUNK, getShuffleRandomKarutaCardsTHUNK, getMemoryShuffleRandomKarutaCardsTHUNK} from "../../store/karutaCards";

export default function GameKarutaMemory({ gameSize }) {
  const dispatch = useDispatch();
  const [displayLanguage, setDisplayLanguage] = useState("english")
  const [firstGuessCard, setFirstGuessCard] = useState("");
  // const [randomCardsArr, setRandomCardsArr] = useState([])
  // const [secondGuessCard, setSecondGuessCard] = useState("");


  const randomCards = useSelector(state => state.karutaCards)
  // retreive a random set of cards depending on the game size
  useEffect(() => {
    dispatch(getMemoryShuffleRandomKarutaCardsTHUNK(gameSize))
    // console.log("use effect")
  }, [dispatch])

  if (!randomCards.random) return null
  if (randomCards.random.length === 0) return null
  console.log("randomCards: ", randomCards.random)
  let randomCardsArr = randomCards.random;
  // console.log("randomCards: ", randomCards)

  return (
    <div className="game-memory-container">
      Hello
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
