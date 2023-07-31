import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { shuffleObj } from "../ComponentFunctions";

import "./GameKarutaMemory.css";
import ComponentGameMemoryKarutaCard from "../ComponentGameMemoryKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { getRandomKarutaCardsTHUNK, getShuffleRandomKarutaCardsTHUNK, getMemoryShuffleRandomKarutaCardsTHUNK, deleteMemoryKarutaCardReducerTHUNK} from "../../store/karutaCards";

export default function GameKarutaMemory({ gameSize }) {
  const dispatch = useDispatch();
  const [displayLanguage, setDisplayLanguage] = useState("english")
  // firstGuessCard for id
  // matchStatus for first or second half of the card
  const [firstGuessCard, setFirstGuessCard] = useState("");
  const [matchStatus, setMatchStatus] = useState("");
  const [correctSelection, setCorrectSelection] = useState("");

  const randomCards = useSelector(state => state.karutaCards)
  // retreive a random set of cards depending on the game size
  useEffect(() => {
    dispatch(getMemoryShuffleRandomKarutaCardsTHUNK(gameSize))
    // console.log("use effect")
  }, [dispatch])

  useEffect(() => {
    dispatch(deleteMemoryKarutaCardReducerTHUNK(correctSelection))
  }, [correctSelection])

  if (!randomCards.random) return null
  if (randomCards.random.length === 0) return null

  let randomCardsArr = randomCards.random;
  // console.log("randomCards: ", randomCards)

  let key = 0;
  return (
    <div className="game-memory-container">
      Hello
      Karuta Memory
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      <div>
        {randomCardsArr.map((card) => {
          key++;
          return <div key={key}>
            <ComponentGameMemoryKarutaCard
              displayLanguage={displayLanguage}
              cardData={card}
              size={'small'}
              gameType={"matchHalf"}
              firstGuessCard={firstGuessCard}
              setFirstGuessCard={setFirstGuessCard}
              matchStatus={matchStatus}
              setMatchStatus={setMatchStatus}
              correctSelection={correctSelection}
              setCorrectSelection={setCorrectSelection} />
          </div>
        })
        }
      </div>
    </div>
  );
}
