import React, { useState, useEffect } from 'react';
import { useModal } from '../../context/Modal';
import { useDispatch, useSelector } from 'react-redux';

import './OpenModalAddCardToDeck.css'
import '../UniversalCSS.css'

import { getDeckTHUNK } from '../../store/decks';
import { getCardsDivideTHUNK, getCardsTHUNK } from '../../store/studyCards';
import ComponentStudyCardPreview from '../ComponentStudyCardPreview';

function OpenModalAddCardToDeck({
  modalComponent, // component to render inside the modal
  buttonText, // text of the button that opens the modal
  onButtonClick, // optional: callback function that will be called once the button that opens the modal is clicked
  onModalClose, // optional: callback function that will be called once the modal is closed

  className,
  cardData,
  editType,
  deckId
}) {
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);
  const cardsAll = useSelector(state => state.studyCards);
  const deck = useSelector(state => state.decks)

  const { closeModal } = useModal();

  const [displayCards, setDisplayCards] = useState("all");
  // all - all deck cards
  // notDeck - cards not in the deck
  // deck - cards in the deck

  useEffect(() => {
    dispatch(getCardsDivideTHUNK(deckId));
    dispatch(getDeckTHUNK(deckId));
  }, [dispatch])

  if (!cardsAll) return null;
  if (!deck) return null

  const handleSubmit = async (e) => {
    e.preventDefault();


    closeModal();
  }

  // All cards
  // all cards includes id's for the cards

// study cards now have deck ids
// display the correct cards based on the deck id
// think about how the deck ids should be used
// possibly normalize this data


  let cards = [];
  if (displayCards === 'all') cards = cardsAll;
  if (displayCards === 'deck') cards = deck.singleDeck.cards
  // if (displayCards === 'notDeck') cards = cardsAll.map(card => card);

  return (
    <div className="open-modal-add-card-to-deck">
      <form
        onSubmit={handleSubmit}>

        <div className="add-card-to-deck-title-selector-container">
          <h2 className={displayCards === "all" ? `add-card-to-deck-${displayCards}-selection` : ''}
            onClick={() => setDisplayCards('all')}>
            All Cards
          </h2>
          <h2 className={displayCards === "notDeck" ?  `add-card-to-deck-${displayCards}-selection` : ''}
            onClick={() => setDisplayCards('notDeck')}>
            Not in Deck Cards
          </h2>
          <h2 className={displayCards === "deck" ?  `add-card-to-deck-${displayCards}-selection` : ''}
            onClick={() => setDisplayCards('deck')} >
            Deck Cards
          </h2>
        </div>

        {/* All cards */}
        <div className="add-card-to-deck-cards-container">
          {Object.values(cards).map(card => {
            return (
              <div>
                <ComponentStudyCardPreview cardData={card} />
              </div>
            )
          })}
        </div>

      </form>
    </div>
  );
}

export default OpenModalAddCardToDeck;
