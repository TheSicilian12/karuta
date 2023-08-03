import React from "react";
import { useDispatch} from 'react-redux';

import "./PoemPracticePage.css";
import GameKarutaMemory from "../GameKarutaMemory";
import LanguageToggle from "../LanguageToggle";

export default function PoemPracticePage() {
  const dispatch = useDispatch();

  return (
    <div className="poem-practice-memory-game">
    Poem Practice
    <GameKarutaMemory gameSize={5}/>
    </div>
  );
}
