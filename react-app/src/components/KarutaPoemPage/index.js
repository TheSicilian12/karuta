import React from "react";
import { useDispatch} from 'react-redux';
import { useParams } from "react-router-dom";

import "./KarutaPoemPage.css";

export default function KarutaPoemPage() {
  const dispatch = useDispatch();

  const {poemId} = useParams()
  console.log("poemId: ", poemId)

  return (
    <div>
    Karuta Poem Page
    
    </div>
  );
}
