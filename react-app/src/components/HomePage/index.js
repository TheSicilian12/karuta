import React, { useEffect } from "react";
import { useDispatch } from 'react-redux';

import { getAllKarutaCardsTHUNK } from "../../store/karutaCards";

import "./HomePage.css";

export default function HomePage() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllKarutaCardsTHUNK())
  }, dispatch)


  return (
   <div>Hello</div>
  );
}
