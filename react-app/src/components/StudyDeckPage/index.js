import React, { useEffect } from "react";
import { useDispatch} from 'react-redux';

import { getAllDecksTHUNK } from "../../store/decks";

import "./StudyDeckPage.css";

export default function StudyDeckPage() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllDecksTHUNK())
  }, [dispatch])

  return (
    <div>
     StudyDeckPage
    </div>
  );
}
