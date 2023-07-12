import { karutaCardNormalizer } from "./storeFunctions"

// constants
const LOAD_KARUTA_CARDS = 'cards/all'
const LOAD_KARUTA_ONE = 'cards/one'

// dispatch
const loadAll = (data) => ({
	type: LOAD_KARUTA_CARDS,
	payload: data
})

const loadOne = (data) => ({
	type: LOAD_KARUTA_ONE,
	payload: data
})

//thunk

// GET all cards THUNK
export const getAllKarutaCardsTHUNK = () => async (dispatch) => {
	const response = await fetch('/api/karuta');
	if (response.ok) {
		const responseJSON = await response.json();
		const responseNormalized = karutaCardNormalizer(responseJSON.cards)
		dispatch(loadAll(responseNormalized))
	}
}

// GET one card THUNK
export const getOneKarutaCardTHUNK = (cardId) => async (dispatch) => {
	// console.log("get one card thunk")
	const response = await fetch(`/api/karuta/${cardId}`)
	if (response.ok) {
		const responseJSON = await response.json();
		// console.log("responseJSON: ", responseJSON)
		const responseNormalized = karutaCardNormalizer(responseJSON)
		dispatch(loadOne(responseNormalized))
	}
}

const initialState = {};

export default function karutaReducer(state = initialState, action) {
	switch (action.type) {
		case LOAD_KARUTA_CARDS: {
			const newState={...action.payload}
			return newState
		}
		case LOAD_KARUTA_ONE: {
			const newState={singleCard: action.payload}
			return newState
		}
		default:
			return state;
	}
}

// state = {
// 	0: {
//		'id': 0,
// 		'author': {
// 			'english': '',
// 			'japanese': '',
// 			'romaji': ''
// 		},
// 		'english': {
// 			0: '',
// 			1: '',
// 			2: '',
// 			3: '',
// 			4: ''
// 		},
// 		'japanese': {
// 			0: '',
// 			1: '',
// 			2: '',
// 			3: '',
// 			4: ''
// 		},
// 		'romaji': {
// 			0: '',
// 			1: '',
// 			2: '',
// 			3: '',
// 			4: ''
// 		}
// 	},
// 	//...
// }
