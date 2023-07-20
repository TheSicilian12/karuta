import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useParams, useHistory } from 'react-router-dom';

import "./MakeCardPage.css";

export default function MakeCardkPage() {
  const dispatch = useDispatch();
  const history = useHistory();

  const { deckId } = useParams()



  return (
    <div>
      Make Card Page
    </div>
  );
}
