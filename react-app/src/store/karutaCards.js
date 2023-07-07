// constants
const LOAD_KARUTA_CARDS = 'cards/all'


// dispatch
const loadAll = (data) => ({
	type: LOAD_KARUTA_CARDS,
	payload: data
})

//thunk

// GET all cards THUNK
export const getAllKarutaCardsTHUNK = () => async (dispatch) => {
	// console.log("get all cards thunk")
	const response = await fetch('/api/karuta');
	if (response.ok) {
		const responseJSON = await response.json();
		dispatch(loadAll(responseJSON))
	}
}

const initialState = {};

export default function karutaReducer(state = initialState, action) {
	switch (action.type) {
		case LOAD_KARUTA_CARDS: {
			const newState={...action.payload}
			return newState
		}
		default:
			return state;
	}
}

// state = {
// 	0: {
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
