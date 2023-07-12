import React from "react";


import "./ComponentKarutaCard.css";

export default function ComponentKarutaCard({displayLanguage, cardData, size}) {
  // ComponentKarutaCard takes in:
  // 1. language
  // 2. data about the card
  // 3. size dimensions for the card

  // Main text should toggle between Japanese and English
  // Change between first card and second card
  // full poem + picture of poet 5-7-5-7-7
  // last two lines 7-7

  if (!cardData) return null

  let cardDimensions = "karuta-card-container"
  if (size === "large") cardDimensions = "karuta-card-container-large"

  const {author} = cardData

  return (
  <div className={`${cardDimensions}`}>
    {displayLanguage === 'english' ? <div>
    {author.english}
    {cardData.english[0]}
    {cardData.english[1]}
    {cardData.english[2]}
    {cardData.english[3]}
    {cardData.english[4]}

    </div> :
    <div>
    {author.japanese}
    {cardData.japanese[0]}
    {cardData.japanese[1]}
    {cardData.japanese[2]}
    {cardData.japanese[3]}
    {cardData.japanese[4]}
    </div>
    }
  </div>
  );
}
