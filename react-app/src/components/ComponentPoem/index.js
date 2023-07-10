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

  if (!cardData) return null

  const { author } = cardData

  const translate = () => {
    setShowTranslation(!showTranslation)
  }

  console.log(showTranslation)

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

          {showTranslation && <div>{cardData.japanese[0]}</div>}
          <div>
            {cardData.english[0]}
          </div>

          {showTranslation && <div>{cardData.japanese[1]}</div>}
          <div>
            {cardData.english[1]}
          </div>

          {showTranslation && <div>{cardData.japanese[2]}</div>}
          <div>
            {cardData.english[2]}
          </div>

          {showTranslation && <div>{cardData.japanese[3]}</div>}
          <div>
            {cardData.english[3]}
          </div>

          {showTranslation && <div>{cardData.japanese[4]}</div>}
          <div>
            {cardData.english[4]}
          </div>
        </div> :
          <div className="displayFlex-column">

            {showTranslation && <div>{cardData.english[0]}</div>}
            <div>
              {cardData.japanese[0]}
            </div>

            {showTranslation && <div>{cardData.english[1]}</div>}
            <div>
              {cardData.japanese[1]}
            </div>

            {showTranslation && <div>{cardData.english[2]}</div>}
            <div>
              {cardData.japanese[2]}
            </div>

            {showTranslation && <div>{cardData.english[3]}</div>}
            <div>
              {cardData.japanese[3]}
            </div>

            {showTranslation && <div>{cardData.english[4]}</div>}
            <div>
              {cardData.japanese[4]}
            </div>
          </div>}
         <button
          onClick={translate}
         >add translation</button>
      </div>
    </div>
  );
}
