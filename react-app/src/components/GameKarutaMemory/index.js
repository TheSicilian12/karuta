import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";

import "./GameKarutaMemory.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { getRandomKarutaCardsTHUNK } from "../../store/karutaCards";
export default function GameKarutaMemory({gameSize}) {
  const dispatch = useDispatch();
  const [displayLanguage, setDisplayLanguage] = useState("english")

  // retreive a random set of cards depending on the game size
  useEffect(() => {
    dispatch(getRandomKarutaCardsTHUNK(gameSize))
  }, [dispatch])

  return (
    <div className="game-memory-container">
      Karuta Memory
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      <ComponentKarutaCard />
    </div>
  );
}
