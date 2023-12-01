import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { shuffleObj } from "../ComponentFunctions";

import "./QuizKaruta.css";
import ComponentGameMemoryKarutaCard from "../ComponentGameMemoryKarutaCard";
import LanguageToggle from "../LanguageToggle";
import { getRandomKarutaCardsTHUNK, getShuffleRandomKarutaCardsTHUNK, getMemoryShuffleRandomKarutaCardsTHUNK, deleteMemoryKarutaCardReducerTHUNK} from "../../store/karutaCards";



export default function QuizKaruta() {
  const dispatch = useDispatch();

  const randomCards = useSelector(state => state.karutaCards)

  useEffect(() => {
    dispatch(getRandomKarutaCardsTHUNK(10))
  }, [dispatch])

  console.log('randomcards: ', randomCards)
  return (
    <div>
      Hello
    </div>
  );
}
