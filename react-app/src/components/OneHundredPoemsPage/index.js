import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getAllKarutaCardsTHUNK } from "../../store/karutaCards";

import "./OneHundredPoemsPage.css";
import "../UniversalCSS.css"
import ComponentKarutaCard from "../ComponentKarutaCard";
import ComponentPoem from "../ComponentPoem";
import LanguageToggle from "../LanguageToggle";
import { Modal } from "../../context/Modal";

export default function OneHundredPoemsPage() {
  const dispatch = useDispatch();
  const [displayLanguage, setDisplayLanguage] = useState("english")
  const [startNum, setStartNum] = useState(1);
  const [endNum, setEndNum] = useState(100)
  const [currentSelection, setCurrentSelection] = useState("1 - 100")

  const cards = useSelector(state => state.karutaCards)

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, [dispatch])

  if (!cards[1]) return null


  const displayCards = (num1, num2) => {
    setStartNum(num1);
    setEndNum(num2);
    setCurrentSelection(`${num1} - ${num2}`)
  }

  return (
    <div>
      <div>
        {currentSelection !== "1 - 100" && <button
          className="button-basic"
          onClick={() => displayCards(1, 100)}
        >
          All
        </button>}
        {currentSelection === "1 - 100" && <button
          className="button-basic button-basic-selected"
          onClick={() => displayCards(1, 100)}
        >
          All
        </button>}

        {currentSelection !== "1 - 10" && <button
          className="button-basic"
          onClick={() => displayCards(1, 10)}
        >
          1 - 10
        </button>}
        {currentSelection === "1 - 10" && <button
          className="button-basic button-basic-selected"
          onClick={() => displayCards(1, 10)}
        >
          1 - 10
        </button>}

        <button
         className="button-basic"
          onClick={() => displayCards(11, 20)}
        >
          11 - 20
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(21, 30)}
        >
          21 - 30
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(31, 40)}
        >
          31 - 40
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(41, 50)}
        >
          41 - 50
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(51, 60)}
        >
          51 - 60
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(61, 70)}
        >
          61 - 70
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(71, 80)}
        >
          71 - 80
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(81, 90)}
        >
          81 - 90
        </button>
        <button
         className="button-basic"
          onClick={() => displayCards(91, 100)}
        >
          91 - 100
        </button>

      </div>
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      {Object.values(cards).map((card) =>
        card.id >= startNum && card.id <= endNum && <div key={card.id}>
          <ComponentPoem language={displayLanguage} cardData={card} />
        </div>
      )}
    </div>
  );
}
