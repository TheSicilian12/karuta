import React, { useEffect } from "react";
import { useDispatch } from 'react-redux';

import "./ComponentKarutaCard.css";

export default function ComponentKarutaCard({language, cardData}) {
  // ComponentKarutaCard takes in:
  // 1. language
  // 2. data about the card

  // Main text should toggle between Japanese and English
  // Change between first card and second card
  // full poem + picture of poet 5-7-5-7-7
  // last two lines 7-7

  if (!cardData) return null

  const {author} = cardData

  return (
  <div className='karuta-card-container'>
    {language === 'english' ? <div>
    {cardData.english[0]}
    {cardData.english[1]}
    </div> :
    <div>
    {cardData.japanese[0]}
    {cardData.japanese[1]}
    </div>
    }
  </div>
  );
}
