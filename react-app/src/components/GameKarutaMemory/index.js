import React, { useEffect, useState } from "react";


import "./GameKarutaMemory.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import LanguageToggle from "../LanguageToggle";

export default function GameKarutaMemory({gameSize}) {
  const [displayLanguage, setDisplayLanguage] = useState("english")

  // retreive a random set of cards depending on the game size
 

  return (
    <div className="game-memory-container">
      Karuta Memory
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      <ComponentKarutaCard />
    </div>
  );
}
