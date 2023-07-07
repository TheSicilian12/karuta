import React, { useEffect } from "react";
import { useDispatch } from 'react-redux';

import "./ComponentKarutaCard.css";

export default function ComponentKarutaCard({cardData}) {
  // Main text should toggle between Japanese and English
  // Change between first card and second card


  if (!cardData) return null

  const {author} = cardData

  // console.log("cardData: ", cardData)
  // console.log("cardData author: ", author)

  return (
  <div className='karuta-card-container'>
    {cardData.english[0]}
    {cardData.english[1]}


  </div>
  );
}
