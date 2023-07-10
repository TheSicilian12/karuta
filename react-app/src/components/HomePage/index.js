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

  const cards = useSelector(state => state.karutaCards)

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, [dispatch])

  if (!cards[1]) return null

  const displayCards = (num1, num2) => {
    console.log(num1, num2)
  }

  return (
   <div>
    <div>
      <button
        onClick={() => displayCards(1, 100)}
      >
        All
        </button>
      <button>
        1 - 10
        </button>
      <button>
        11 - 20
        </button>
      <button>
        21 - 30
        </button>
      <button>
        31 - 40
        </button>
      <button>
        41 - 50
        </button>
      <button>
        51 - 60
        </button>
      <button>
        61 - 70
        </button>
      <button>
        71 - 80
        </button>
      <button>
        81 - 90
        </button>
      <button>
        91 - 100
        </button>

    </div>
    <LanguageToggle displayLanguage={displayLanguage} setDisplayLanguage={setDisplayLanguage} languageOne={"english"} languageTwo={"japanese"} />
    {Object.values(cards).map((card) =>
    <div>
      <ComponentKarutaCard language={displayLanguage} cardData={card} />
      </div>)}
    </div>
  );
}
