import React, { useEffect } from "react";
import { useDispatch, useSelector} from 'react-redux';

import { getCurrentUserDecksTHUNK } from "../../store/decks";

import "./StudyDeckPage.css";

export default function StudyDeckPage() {
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);
  console.log("session: ", sessionUser)
  useEffect(() => {
    dispatch(getCurrentUserDecksTHUNK(sessionUser.id))
  }, [dispatch])

  return (
    <div>
     StudyDeckPage
    </div>
  );
}
