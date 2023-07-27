import { normalizer } from "./storeFunctions";

// constants
const LOAD_DECKS = 'decks/all'
const LOAD_ONE = 'decks/one'

// dispatch
const loadAll = (data) => ({
	type: LOAD_DECKS,
	payload: data
})

const loadOne = (data) => ({
	type: LOAD_ONE,
	payload: data
})

//thunk

// GET all of a users decks THUNK
export const getCurrentUserDecksTHUNK = (userId) => async (dispatch) => {
	const response = await fetch(`/api/decks/user/${userId}`);
	if (response.ok) {
		const responseJSON = await response.json();
		const responseNormalized = normalizer(responseJSON);
		dispatch(loadAll(responseNormalized))
	}
}

// GET a specific deck THUNK
export const getDeckTHUNK = (deckId) => async (dispatch) => {
	const response = await fetch(`/api/decks/${deckId}`);
	if (response.ok) {
		const responseJSON = await response.json();
		dispatch(loadOne(responseJSON))
	}
}

const initialState = {};

export default function studyDeckReducer(state = initialState, action) {
	switch (action.type) {
		case LOAD_DECKS: {
			const newState = { ...action.payload }
			return newState
		}
		case LOAD_ONE: {
			const newState = { singleDeck: {...action.payload} }
			return newState
		}
		default:
			return state;
	}
}
