import React, { useState } from "react";

import "./ComponentPoem.css";
import "../UniversalCSS.css";

export default function ComponentPoem({ language, cardData }) {
  // ComponentPoem takes in:
  // 1. language
  // 2. data about the card

  // Main text should toggle between Japanese and English
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
      <div className="karuta-main-text-poem-container">
      <div className="displayFlex">
          <button
            onClick={translate}>
            add translation
          </button>

          {(language === 'japanese' ||
            showRomaji === true ||
            (language === 'english' && showTranslation === true))
            &&
            <button
              onClick={addRomaji}
            >
              romaji
            </button>}
        </div>
        {language === 'english' ? <div className="displayFlex-column">
          <div className="karuta-main-text-line">
            {showRomaji && <div>{cardData.romaji[0]}</div>}
            {showTranslation && <div>{cardData.japanese[0]}</div>}
            <div className="karuta-main-text-emphasis">
              {cardData.english[0]}
            </div>
          </div>

          <div className="karuta-main-text-line">
            {showRomaji && <div>{cardData.romaji[1]}</div>}
            {showTranslation && <div>{cardData.japanese[1]}</div>}
            <div className="karuta-main-text-emphasis">
              {cardData.english[1]}
            </div>
          </div>

          <div className="karuta-main-text-line">
            {showRomaji && <div>{cardData.romaji[2]}</div>}
            {showTranslation && <div>{cardData.japanese[2]}</div>}
            <div className="karuta-main-text-emphasis">
              {cardData.english[2]}
            </div>
          </div>

          <div className="karuta-main-text-line">
            {showRomaji && <div>{cardData.romaji[3]}</div>}
            {showTranslation && <div>{cardData.japanese[3]}</div>}
            <div className="karuta-main-text-emphasis">
              {cardData.english[3]}
            </div>
          </div>

          <div className="karuta-main-text-line">
            {showRomaji && <div>{cardData.romaji[4]}</div>}
            {showTranslation && <div>{cardData.japanese[4]}</div>}
            <div className="karuta-main-text-emphasis">
              {cardData.english[4]}
            </div>
          </div>

          <div className="karuta-main-text-line">
            {showRomaji && <div>{author.romaji}</div>}
            {showTranslation && <div>{author.japanese}</div>}
            <div className="karuta-main-text-emphasis">
              {author.english}
            </div>
          </div>
        </div> :
          <div className="displayFlex-column">

            <div className="karuta-main-text-line">
              {showTranslation && <div>{cardData.english[0]}</div>}
              {showRomaji && <div>{cardData.romaji[0]}</div>}
              <div className="karuta-main-text-emphasis">
                {cardData.japanese[0]}
              </div>
            </div>

            <div className="karuta-main-text-line">
              {showTranslation && <div>{cardData.english[1]}</div>}
              {showRomaji && <div>{cardData.romaji[1]}</div>}
              <div className="karuta-main-text-emphasis">
                {cardData.japanese[1]}
              </div>
            </div>

            <div className="karuta-main-text-line">
              {showTranslation && <div>{cardData.english[2]}</div>}
              {showRomaji && <div>{cardData.romaji[2]}</div>}
              <div className="karuta-main-text-emphasis">
                {cardData.japanese[2]}
              </div>
            </div>

            <div className="karuta-main-text-line">
              {showTranslation && <div>{cardData.english[3]}</div>}
              {showRomaji && <div>{cardData.romaji[3]}</div>}
              <div className="karuta-main-text-emphasis">
                {cardData.japanese[3]}
              </div>
            </div>

            <div className="karuta-main-text-line">
              {showTranslation && <div>{cardData.english[4]}</div>}
              {showRomaji && <div>{cardData.romaji[4]}</div>}
              <div className="karuta-main-text-emphasis">
                {cardData.japanese[4]}
              </div>
            </div>

            <div className="karuta-main-text-line">
              {showTranslation && <div>{author.english}</div>}
              {showRomaji && <div>{author.romaji}</div>}
              <div className="karuta-main-text-emphasis">
                {author.japanese}
              </div>
            </div>
          </div>}

        {/* <div className="displayFlex-column">
          <button
            onClick={translate}>
            add translation
          </button>

          {(language === 'japanese' ||
            showRomaji === true ||
            (language === 'english' && showTranslation === true))
            &&
            <button
              onClick={addRomaji}
            >
              romaji
            </button>}
        </div> */}
      </div>
    </div>
  );
}
