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
import LoginFormPage from "./components/LoginFormPage";

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
          <Route path="/login" exact>
            <LoginFormPage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
