import React, { useEffect } from "react";
import { useDispatch } from 'react-redux';

import "./ComponentKarutaCard.css";

export default function ComponentKarutaCard({cardData}) {

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
