import { normalizer } from "./storeFunctions";

// constants
const LOAD_DECKS = 'cards/all'

// dispatch
const loadAll = (data) => ({
	type: LOAD_DECKS,
	payload: data
})

//thunk

// GET all of a users cards THUNK
export const getCurrentUserDecksTHUNK = (userId) => async (dispatch) => {
	const response = await fetch(`/api/decks/${userId}`);
	if (response.ok) {
		const responseJSON = await response.json();
		const responseNormalized = normalizer(responseJSON);
		dispatch(loadAll(responseNormalized))
	}
}

const initialState = {};

export default function studyDeckReducer(state = initialState, action) {
	switch (action.type) {
		case LOAD_DECKS: {
			const newState = { ...action.payload }
			return newState
		}
		default:
			return state;
	}
}
