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
  const [endNum, setEndNum] = useState(10)
  const [currentSelection, setCurrentSelection] = useState("1 - 10")

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
      <div className="poems-page-nav-buttons-container">
        <div>
         <button
            className={currentSelection === "1 - 100" ? "button-basic-selected poems-page-nav-buttons" :
                                                      "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(1, 100)}
          >
            All
          </button>
        </div>

        <div className='poems-page-nav-group'>
         <button
            className={currentSelection === "1 - 10" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(1, 10)}
          >
            1 - 10
          </button>

          <button
            className={currentSelection === "11 - 20" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(11, 20)}
          >
            11 - 20
          </button>

         <button
            className={currentSelection === "21 - 30" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(21, 30)}
          >
            21 - 30
          </button>

         <button
            className={currentSelection === "31 - 40" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(31, 40)}
          >
            31 - 40
          </button>

          <button
            className={currentSelection === "41 - 50" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(41, 50)}
          >
            41 - 50
          </button>

          <button
            className={currentSelection === "51 - 60" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(51, 60)}
          >
            51 - 60
          </button>

          <button
            className={currentSelection === "61 - 70" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(61, 70)}
          >
            61 - 70
          </button>

          <button
            className={currentSelection === "71 - 80" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(71, 80)}
          >
            71 - 80
          </button>

          <button
            className={currentSelection === "81 - 90" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(81, 90)}
          >
            81 - 90
          </button>

          <button
            className={currentSelection === "91 - 100" ? "button-basic-selected poems-page-nav-buttons" :
            "button-basic poems-page-nav-buttons"}
            onClick={() => displayCards(91, 100)}
          >
            91 - 100
          </button>
        </div>
      </div>
      <div className="poems-page-poems-container">
        <div className="poems-page-toggle">
          <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
        </div>
        {Object.values(cards).map((card) =>
          card.id >= startNum && card.id <= endNum && <div
            className="poems-page-poem-margin "
            key={card.id}>
            <ComponentPoem language={displayLanguage} cardData={card} />

          </div>
        )}
      </div>
    </div>
  );
}
