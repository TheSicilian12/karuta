import React, { useEffect } from "react";
import { useDispatch} from 'react-redux';
import { useParams } from "react-router-dom";

import "./KarutaPoemPage.css";
import ComponentKarutaCard from "../ComponentKarutaCard";
import {getOneKarutaCardTHUNK} from "../../store/karutaCards"

export default function KarutaPoemPage() {
  const dispatch = useDispatch();

  const {poemId} = useParams()

  useEffect(() => {
    dispatch(getOneKarutaCardTHUNK(poemId))
  }, [dispatch])


  return (
    <div>
    Karuta Poem Page
    {/* <ComponentKarutaCard displayLanguage={displayLanguage} cardData={card}/> */}
    </div>
  );
}
