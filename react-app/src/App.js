import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import { authenticate } from "./store/session";
import OneHundredPoemsPage from "./components/OneHundredPoemsPage";
import Navigation from "./components/Navigation";
import HomePage from "./components/Homepage";
import PoemPracticePage from "./components/PoemPracticePage";
import KarutaPoemPage from "./components/KarutaPoemPage";
import StudyDeckPage from "./components/StudyDeckPage";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      {isLoaded && (
        <Switch>
          <Route path="/" exact>
            <Navigation />
            <HomePage />
          </Route>
          <Route path="/100poems" exact>
            <Navigation />
            <OneHundredPoemsPage />
          </Route>
          <Route path="/100poems/:poemId" exact>
            <Navigation />
            <KarutaPoemPage />
          </Route>
          <Route path="/poempractice" exact>
            <Navigation />
            <PoemPracticePage />
          </Route>
          <Route path="/studyDecks" exact>
            <Navigation />
            <StudyDeckPage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
