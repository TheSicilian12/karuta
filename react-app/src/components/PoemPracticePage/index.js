import React from "react";
import { useDispatch} from 'react-redux';

import "./PoemPracticePage.css";
import GameKarutaMemory from "../GameKarutaMemory";

export default function PoemPracticePage() {
  const dispatch = useDispatch();

  return (
    <div>
    Poem Practice
    <GameKarutaMemory />
    </div>
  );
}
