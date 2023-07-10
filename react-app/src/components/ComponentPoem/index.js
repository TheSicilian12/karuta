import React, { useState } from "react";

import "./ComponentPoem.css";
import "../UniversalCSS.css";

export default function ComponentPoem({ language, cardData }) {
  // ComponentPoem takes in:
  // 1. language
  // 2. data about the card

  // Main text should toggle between Japanese and English
  // Change between first card and second card
  // full poem + picture of poet 5-7-5-7-7
  // last two lines 7-7
  const [showTranslation, setShowTranslation] = useState(false)
  const [showRomaji, setShowRomaji] = useState(false)

  if (!cardData) return null

  const { author } = cardData

  const translate = () => {
    setShowTranslation(!showTranslation)
  }

  const addRomaji = () => {
    setShowRomaji(!showRomaji)
  }

  return (
    <div className="displayFlex">
      <div className='karuta-card-poem-container'>
        {language === 'english' ?
          <div>
            {cardData.english[0]}
            {cardData.english[1]}
          </div> :
          <div>
            {cardData.japanese[0]}
            {cardData.japanese[1]}
          </div>
        }
      </div>
      <div className="karuta-main-text-poem-container">
        {language === 'english' ? <div className="displayFlex-column">

          {showRomaji && <div>{cardData.romaji[0]}</div>}
          {showTranslation && <div>{cardData.japanese[0]}</div>}
          <div>
            {cardData.english[0]}
          </div>

          {showRomaji && <div>{cardData.romaji[1]}</div>}
          {showTranslation && <div>{cardData.japanese[1]}</div>}
          <div>
            {cardData.english[1]}
          </div>

          {showRomaji && <div>{cardData.romaji[2]}</div>}
          {showTranslation && <div>{cardData.japanese[2]}</div>}
          <div>
            {cardData.english[2]}
          </div>

          {showRomaji && <div>{cardData.romaji[3]}</div>}
          {showTranslation && <div>{cardData.japanese[3]}</div>}
          <div>
            {cardData.english[3]}
          </div>

          {showRomaji && <div>{cardData.romaji[4]}</div>}
          {showTranslation && <div>{cardData.japanese[4]}</div>}
          <div>
            {cardData.english[4]}
          </div>

          {showRomaji && <div>{author.romaji}</div>}
          {showTranslation && <div>{author.japanese}</div>}
          <div>
            {author.english}
          </div>
        </div> :
          <div className="displayFlex-column">

            {showTranslation && <div>{cardData.english[0]}</div>}
            {showRomaji && <div>{cardData.romaji[0]}</div>}
            <div>
              {cardData.japanese[0]}
            </div>

            {showTranslation && <div>{cardData.english[1]}</div>}
            {showRomaji && <div>{cardData.romaji[1]}</div>}
            <div>
              {cardData.japanese[1]}
            </div>

            {showTranslation && <div>{cardData.english[2]}</div>}
            {showRomaji && <div>{cardData.romaji[2]}</div>}
            <div>
              {cardData.japanese[2]}
            </div>

            {showTranslation && <div>{cardData.english[3]}</div>}
            {showRomaji && <div>{cardData.romaji[3]}</div>}
            <div>
              {cardData.japanese[3]}
            </div>

            {showTranslation && <div>{cardData.english[4]}</div>}
            {showRomaji && <div>{cardData.romaji[4]}</div>}
            <div>
              {cardData.japanese[4]}
            </div>

            {showTranslation && <div>{author.english}</div>}
            {showRomaji && <div>{author.romaji}</div>}
            <div>
              {author.japanese}
            </div>
          </div>}

        <button
          onClick={translate}>
            add translation
        </button>

        {(language === 'japanese' ||
        (language === 'english' && showTranslation === true)) &&
        <button
          onClick={addRomaji}
        >
          romaji
        </button>}
      </div>
    </div>
  );
}
