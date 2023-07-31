import { normalizer } from "./storeFunctions";

// constants
const GET_USERS = 'cards/users'
const EDIT_ONE = 'cards/edit'
const DELETE_ONE = 'cards/delete'

// dispatch
const getUsers = (data) => ({
	type: GET_USERS,
	payload: data
})

const editOne = (data) => ({
	type: EDIT_ONE,
	payload: data
})

const deleteOne = (data) => ({
	type: DELETE_ONE,
	payload: data
})


//thunk

// GET a users cards THUNK
export const getCardsTHUNK = () => async (dispatch) => {
	console.log("----getCardsTHUNK----")
	let response = await fetch ('/api/study_cards/users');
	if (response.ok) {
		const data = await response.json();
		const normalizedData = normalizer(data)
		// console.log("normalizedData: ", normalizedData);
		dispatch(getUsers(normalizedData));
	}
}

// GET a users cards and divide by deck status THUNK
export const getCardsDivideTHUNK = (deckId) => async (dispatch) => {
	console.log("----getCardsDivideTHUNK----")
	let response = await fetch ('/api/study_cards/users');
	if (response.ok) {
		deckId = Number(deckId);
		// console.log("deckId: ", deckId)
		let cardObj = {};

		const data = await response.json();
		const normalizedData = normalizer(data)
		// console.log("normalizedData: ", normalizedData);

		cardObj["all"] = {...normalizedData};
		cardObj = {
			"all": {...normalizedData},
			"notDeck": {},
			"inDeck": {}
		}

		for (const card in normalizedData) {
			// console.log("card: ", normalizedData[card].decks)
			// console.log("card decks includes: ", normalizedData[card].decks.includes(1))
			// console.log("deckId: ", typeof deckId)
			if (normalizedData[card].decks.includes(deckId)) {
				// console.log("includes")
				// console.log(normalizedData[card].id)
				cardObj.inDeck[normalizedData[card].id] = normalizedData[card];
			} else {
				cardObj.notDeck[normalizedData[card].id] = normalizedData[card];
			}
		}
		// console.log("cardObj: ", cardObj)

		dispatch(getUsers(cardObj));
	}
}


// ADD a card THUNK
export const addCardTHUNK = (cardData) => async (dispatch) => {
	// this may or may not associate with a deck

	// make the card
	// if there is a deckId then associateCardDeckTHUNK
	// if there is not a deckId then don't associate
	console.log("----addCardThunk----")
	const {question, answer, answerLong, ownerId} = cardData;
	// console.log("cardData: ", cardData)
	let payload = {
		question,
		answer,
		answer_long: answerLong,
		owner_id: ownerId
	}

	let response = await fetch(`/api/study_cards/post`, {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(
			payload
		)
	})

	if (response.ok) {
		const data = await response.json();
		console.log("data: ", data)

		if (cardData.deckId) {
			let card = data.card;
			let deckId = cardData.deckId;

			console.log("card: ", card)
			console.log("deck: ", deckId)
			dispatch(associateCardDeckTHUNK(card, deckId))
		}
	}
}

// ASSOCIATE a card with a deck THUNK
export const associateCardDeckTHUNK = (cardData, deckId) => async (dispatch) => {
	console.log("----associate card deck thunk---")
	const cardId = cardData.id;

	let response = await fetch(`/api/study_cards/associate/card/${cardId}/deck/${deckId}`, {
		method: "PUT",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(
			cardData
		)
	})
}

// DISASSOCIATE a card from a deck THUNK
export const disassociateCardDeckTHUNK = (cardId, deckId) => async (dispatch) => {
	console.log("----disassociate card deck thunk----")

	const response = await fetch (`/api/study_cards/associate/card/${cardId}/deck/${deckId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        }
    })
}

// EDIT a users card THUNK
export const editCardQuestionTHUNK = (cardData) => async (dispatch) => {
	const {cardId, ownerId, question, answer, answer_long} = cardData
	console.log('edit study card THUNK')
	const payload = {
		owner_id: ownerId,
		question,
		answer_long,
		answer
	}
	console.log("cardId: ", cardId)

	const response = await fetch(`/api/study_cards/${cardId}`, {
		method: "PUT",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(
			payload
		)
	})

	if (response.ok) {
		const data = await response.json();
		console.log("data: ", data)
	}
}

// DELETE a card THUNK
export const deleteCardTHUNK = (cardId) => async (dispatch) => {
	console.log("----delete card thunk---")
	const response = await fetch (`/api/study_cards/${cardId}`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        }
    })
	if (response.ok) {
		const data = await response.json();
		// console.log("data: ", data)
		dispatch(deleteOne(data.card_id));
	}
}


const initialState = {};

export default function studyCardReducer(state = initialState, action) {
	switch (action.type) {
		case GET_USERS: {
			const newState = { ...action.payload }
			return newState
		}
		case EDIT_ONE: {
			const newState = { ...action.payload }
			return newState
		}
		case DELETE_ONE: {
			console.log(action.payload)
			// console.log("state: ", state)
			delete state[`${action.payload}`]
			const newState = {...state}
			return newState
		}
		default:
			return state;
	}
}
