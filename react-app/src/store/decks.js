// constants
const LOAD_DECKS = 'cards/all'

// dispatch
const loadAll = (data) => ({
	type: LOAD_DECKS,
	payload: data
})

//thunk

// GET all cards THUNK
export const getAllDecksTHUNK = () => async (dispatch) => {
	const response = await fetch('/api/decks');
	if (response.ok) {
		const responseJSON = await response.json();
		dispatch(loadAll(responseJSON))
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
