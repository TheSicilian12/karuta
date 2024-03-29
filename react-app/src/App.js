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
import DeckPage from "./components/DeckPage";
import MakeCardPage from "./components/MakeCardPage";
import MakeDeckPage from "./components/MakeDeckPage";
import MakeCardPageWrapper from "./components/MakeCardPage/MakeCardWrapper";
import LoginFormPage from "./components/LoginFormPage";
import StudyCardDeckPage from "./components/StudyCardDeckPage";

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
            <Navigation isLoaded={isLoaded}/>
            <HomePage />
          </Route>
          <Route path="/100poems" exact>
            <Navigation isLoaded={isLoaded}/>
            <OneHundredPoemsPage />
          </Route>
          <Route path="/100poems/:poemId" exact>
            <Navigation isLoaded={isLoaded}/>
            <KarutaPoemPage />
          </Route>
          <Route path="/poempractice" exact>
            <Navigation isLoaded={isLoaded}/>
            <PoemPracticePage />
          </Route>
          <Route path="/studyDecks" exact>
            <Navigation isLoaded={isLoaded}/>
            <StudyDeckPage />
          </Route>
          <Route path="/studyDecks/:deckId" exact>
            <Navigation isLoaded={isLoaded}/>
            <DeckPage />
          </Route>
          <Route path="/makeCard/:deckId" exact>
            <Navigation isLoaded={isLoaded}/>
            <MakeCardPageWrapper />
          </Route>
          <Route path="/makeCard/" exact>
            <Navigation isLoaded={isLoaded}/>
            <MakeCardPage />
          </Route>
          <Route path="/makeDeck/" exact>
            <Navigation isLoaded={isLoaded}/>
            <MakeDeckPage />
          </Route>
          <Route path="/study/:deckId" exact>
            <Navigation isLoaded={isLoaded}/>
            <StudyCardDeckPage />
          </Route>
          <Route path="/login" exact>
            <LoginFormPage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
