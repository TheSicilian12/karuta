import React, { useContext, useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';

import { getAllKarutaCardsTHUNK } from "../../store/karutaCards";

import "./HomePage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { Modal } from "../../context/Modal";

export default function HomePage() {
  const dispatch = useDispatch();
  const [displayLanguage, setDisplayLanguage] = useState("english")
  const [startNum, setStartNum] = useState(1);
  const [endNum, setEndNum] = useState(100)

  const cards = useSelector(state => state.karutaCards)

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, [dispatch])

  if (!cards[1]) return null


  const displayCards = (num1, num2) => {
    setStartNum(num1);
    setEndNum(num2);
  }

  // Object.values(cards).map((card) => console.log(card.id))

  return (
    <div>
      <div>
        <button
          onClick={() => displayCards(1, 100)}
        >
          All
        </button>
        <button
          onClick={() => displayCards(1, 10)}
        >
          1 - 10
        </button>
        <button
          onClick={() => displayCards(11, 20)}
        >
          11 - 20
        </button>
        <button
          onClick={() => displayCards(21, 30)}
        >
          21 - 30
        </button>
        <button
          onClick={() => displayCards(31, 40)}
        >
          31 - 40
        </button>
        <button
          onClick={() => displayCards(41, 50)}
        >
          41 - 50
        </button>
        <button
          onClick={() => displayCards(51, 60)}
        >
          51 - 60
        </button>
        <button
          onClick={() => displayCards(61, 70)}
        >
          61 - 70
        </button>
        <button
          onClick={() => displayCards(71, 80)}
        >
          71 - 80
        </button>
        <button
          onClick={() => displayCards(81, 90)}
        >
          81 - 90
        </button>
        <button
          onClick={() => displayCards(91, 100)}
        >
          91 - 100
        </button>

      </div>
      <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
      {Object.values(cards).map((card) =>
        // {console.log(typeof card.id)}
        card.id >= startNum && card.id <= endNum && <div>
          <ComponentKarutaCard language={displayLanguage} cardData={card} />
        </div>
      )}
    </div>
  );
}
