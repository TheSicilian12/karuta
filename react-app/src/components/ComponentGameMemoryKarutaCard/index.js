import React, { useEffect, useRef, useState } from "react";
import { useDispatch } from "react-redux";

import "./ComponentGameMemoryKarutaCard.css";
import { deleteMemoryKarutaCardReducerTHUNK } from "../../store/karutaCards";

export default function ComponentGameMemoryKarutaCard({ displayLanguage, cardData, size, gameType, firstGuessCard, setFirstGuessCard, matchStatus, setMatchStatus, correctSelection, setCorrectSelection }) {
  // ComponentKarutaCard takes in:
  // 1. language
  // 2. data about the card
  // 3. size dimensions for the card
  // 4. what game style to play

  // game types:
  // 1. "matchHalf" - match the first part of the poem with the second part of the poem


  // game:
  // will need to display the different sets of cards, so render double the number of cards
  // will need to be able to have the cards displayed in a random order together
  const cardRef = useRef();

  const [display, setDisplay] = useState(false)

  useEffect(() => {
    function handleClickOutside(event) {
      if (cardRef.current && !cardRef.current.contains(event.target)) {
        setDisplay(false);
      }
    }

    document.addEventListener("click", handleClickOutside);

    return () => {
      document.removeEventListener("click", handleClickOutside);
    }

  }, []);



  if (!cardData) return null

  let cardDimensions = "karuta-card-container"
  if (size === "large") cardDimensions = "karuta-card-container-large"

  const { author, match } = cardData

  const AnswerCheck = () => {
    // two guesses. If the second doesn't match the first's id then fail
    // reset data

    // first guess
    // if it does not exist, set it
    // if it does exist, check the current card id
    // const dispatch = useDispatch();

    console.log("answer check")
    if (!firstGuessCard) {
      setFirstGuessCard(cardData.id);
      setMatchStatus(cardData.match);
    } else if (firstGuessCard === cardData.id && matchStatus !== cardData.match) {
      console.log("got the card!")
      // dispatch(deleteMemoryKarutaCardReducerTHUNK(firstGuessCard));
      setCorrectSelection(firstGuessCard);
      setFirstGuessCard("");
      setMatchStatus("");
    } else {
      setFirstGuessCard("");
      setMatchStatus("");
    }

  }

  const flipCard = () => {
    // A card needs to start covered
    // on click it is revealed
    // when any other card is clicked it is hidden again

    console.log("flip card")

    setDisplay(!display)

    if (!display) AnswerCheck();
  }
  // console.log("display: ", display)
  // console.log("first guess: ", firstGuessCard)
  // console.log("card: ", cardData.id)

  return (
    <div ref={cardRef} onClick={() => flipCard()}>
    <div
      onClick={() => flipCard()}>
      {display !== true ? <div className={`${cardDimensions} memory-game-container memory-game-container-card-back`}></div> :

        <div className={`${cardDimensions} memory-game-container`}
          // onClick={AnswerCheck}
        >
          {displayLanguage === 'english' ? <div className="displayFlex-column">
            {/* matchHalf, match the first part of the poem with the second */}
            {gameType === 'matchHalf' &&
              <div>
                {match === true && <div>
                  <div>{cardData.english[0]}</div>
                </div>}
                {match === false && <div>
                  <div>{cardData.english[3]}</div>
                  <div>{cardData.english[4]}</div>
                </div>}
              </div>}
          </div>
            :
            <div className="vertical-writing-rl">
              {/* matchHalf, match the first part of the poem with the second */}
              {gameType === 'matchHalf' && <div>
                {match === true && <div>
                  <div>{cardData.japanese[0]}</div>
                </div>}
                {match === false && <div>
                  <div>{cardData.japanese[3]}</div>
                  <div>{cardData.japanese[4]}</div>
                </div>}
              </div>}
            </div>
          }
        </div >
      }
    </div>
    </div>
  );
}
