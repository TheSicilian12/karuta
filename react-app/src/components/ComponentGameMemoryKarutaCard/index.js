import React from "react";


import "./ComponentGameMemoryKarutaCard.css";

export default function ComponentGameMemoryKarutaCard({ displayLanguage, cardData, size, gameType, firstGuessCard, setFirstGuessCard }) {
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


  if (!cardData) return null

  let cardDimensions = "karuta-card-container"
  if (size === "large") cardDimensions = "karuta-card-container-large"

  const { author, match } = cardData

  const answerCheck = () => {
    if (!firstGuessCard) setFirstGuessCard(cardData.id);
    else {
      if (firstGuessCard === cardData.id) console.log("got the card!")
      else setFirstGuessCard("")
    }
  }

  console.log("first guess: ", firstGuessCard)
  console.log("card: ", cardData.id)

  return (
    <div className={`${cardDimensions} memory-game-container`}
          onClick={answerCheck}
    >
      {displayLanguage === 'english' ? <div className="displayFlex-column">
        {/* matchHalf, match the first part of the poem with the second */}
        {gameType === 'matchHalf' && <div>
          {match === 'first' && <div>
            <div>{cardData.english[0]}</div>
          </div>}
          {match === 'second' && <div>
            <div>{cardData.english[3]}</div>
            <div>{cardData.english[4]}</div>
            </div>}
        </div>}
      </div>
        :
        <div className="vertical-writing-rl">
          {/* matchHalf, match the first part of the poem with the second */}
          {gameType === 'matchHalf' && <div>
          {match === 'first' && <div>
            <div>{cardData.japanese[0]}</div>
          </div>}
          {match === 'second' && <div>
            <div>{cardData.japanese[3]}</div>
            <div>{cardData.japanese[4]}</div>
            </div>}
        </div>}
        </div>
      }

    </div>
  );
}
