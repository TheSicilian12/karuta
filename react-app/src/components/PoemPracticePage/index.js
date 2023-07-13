import React from "react";
import { useDispatch} from 'react-redux';

import "./PoemPracticePage.css";
import GameKarutaMemory from "../GameKarutaMemory";
import LanguageToggle from "../LanguageToggle";

export default function PoemPracticePage() {
  const dispatch = useDispatch();

  return (
    <div>
    Poem Practice
    <GameKarutaMemory gameSize={10}/>
    </div>
  );
}
