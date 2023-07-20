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
		case EDIT_ONE: {
			const newState = { ...action.payload }
			return newState
		}
		default:
			return state;
	}
}
