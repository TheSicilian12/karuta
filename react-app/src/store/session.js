// constants
const LOAD_KARUTA_CARDS = 'cards/all'





const initialState = {};

export default function karutaReducer(state = initialState, action) {
	switch (action.type) {
		case SET_USER:
			return { user: action.payload };
		case REMOVE_USER:
			return { user: null };
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
