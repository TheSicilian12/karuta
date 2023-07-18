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

  const { author } = cardData

  return (
    <div className={`${cardDimensions} memory-game-container`}>
      {displayLanguage === 'english' ? <div className="displayFlex-column">
        {/* {!poemDisplay && <div>
          <div>{author.english}</div>
          <div>{cardData.english[0]}</div>
          <div>{cardData.english[1]}</div>
          <div>{cardData.english[2]}</div>
          <div>{cardData.english[3]}</div>
          <div>{cardData.english[4]}</div>
        </div>}
        {poemDisplay === 'first' && <div>
          <div>{cardData.english[0]}</div>
        </div>}
        {poemDisplay === 'second' && <div>
          <div>{cardData.english[3]}</div>
          <div>{cardData.english[4]}</div>
        </div>} */}

        {gameType === 'halfMatch' && <div>

        </div>}
      </div>
        :
        <div className="vertical-writing-rl">
          {/* {!poemDisplay && <div>
            <div>{author.japanese}</div>
            <div>{cardData.japanese[0]}</div>
            <div>{cardData.japanese[1]}</div>
            <div>{cardData.japanese[2]}</div>
            <div>{cardData.japanese[3]}</div>
            <div>{cardData.japanese[4]}</div>
          </div>}
          {poemDisplay === 'first' && <div>
            <div>{cardData.japanese[0]}</div>
          </div>}
          {poemDisplay === 'second' && <div>
            <div>{cardData.japanese[3]}</div>
            <div>{cardData.japanese[4]}</div>
          </div>} */}
        </div>
      }

    </div>
  );
}
