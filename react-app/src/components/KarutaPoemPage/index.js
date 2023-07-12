import React, { useEffect } from "react";
import { useDispatch, useSelector} from 'react-redux';
import { useParams } from "react-router-dom";

import "./KarutaPoemPage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import {getOneKarutaCardTHUNK} from "../../store/karutaCards"

export default function KarutaPoemPage() {
  const dispatch = useDispatch();

  const {poemId} = useParams()
  const cardData = useSelector(state => state.karutaCards.singleCard)
  useEffect(() => {
    dispatch(getOneKarutaCardTHUNK(poemId))
  }, [dispatch])

  if (!cardData) return null

  return (
    <div>
    Karuta Poem Page
    <ComponentKarutaCard displayLanguage={"english"} cardData={cardData[poemId]}/>
    </div>
  );
}
