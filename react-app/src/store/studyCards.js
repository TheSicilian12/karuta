import { normalizer } from "./storeFunctions";

// constants
const EDIT_ONE = 'cards/edit'


// dispatch
const editOne = (data) => ({
	type: EDIT_ONE,
	payload: data
})


//thunk

// EDIT a users card THUNK
export const editCardQuestionTHUNK = (cardData) => async (dispatch) => {
	const {cardId, question} = cardData


	const response = await fetch(`/api/study_cards/${cardId}`, {
		method: "PUT",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify(
			cardData
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
		case EDIT_ONE: {
			const newState = { ...action.payload }
			return newState
		}
		default:
			return state;
	}
}
