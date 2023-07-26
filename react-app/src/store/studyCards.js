import { normalizer } from "./storeFunctions";

// constants
const GET_USERS = 'cards/users'
const EDIT_ONE = 'cards/edit'

// dispatch
const getUsers = (data) => ({
	type: GET_USERS,
	payload: data
})

const editOne = (data) => ({
	type: EDIT_ONE,
	payload: data
})


//thunk

// GET a users cards THUNK
export const getCardsTHUNK = (userId) => async (dispatch) => {
	console.log("----getCardsTHUNK----")
	let response = await fetch ('/api/study_cards/users');
	if (response.ok) {
		const data = await response.json();
		const normalizedData = normalizer(data)
		// console.log("normalizedData: ", normalizedData);
		dispatch(getUsers(normalizedData));
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
		default:
			return state;
	}
}
