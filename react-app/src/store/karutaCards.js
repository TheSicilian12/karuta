import { shuffleObj } from "../components/ComponentFunctions"
import { karutaCardNormalizer } from "./storeFunctions"

// constants
const LOAD_KARUTA_CARDS = 'cards/all'
const LOAD_KARUTA_ONE = 'cards/one'
const LOAD_RANDOM_SHUFFLE = 'cards/randomShuffle'

// dispatch
const loadAll = (data) => ({
	type: LOAD_KARUTA_CARDS,
	payload: data
})

const loadOne = (data) => ({
	type: LOAD_KARUTA_ONE,
	payload: data
})

const loadRandomShuffle = (data) => ({
	type: LOAD_RANDOM_SHUFFLE,
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

// GET a specific amount of random cards THUNK
export const getRandomKarutaCardsTHUNK = (cardAmount) => async (dispatch) => {
	const response = await fetch(`/api/karuta/random/${cardAmount}`)
	if (response.ok) {
		const responseJSON = await response.json();
		const responseNormalized = karutaCardNormalizer(responseJSON.cards)
		dispatch(loadAll(responseNormalized))
	}
}

// GET and shuffle cards - OUTPUT: ARRAY
export const getShuffleRandomKarutaCardsTHUNK = (cardAmount) => async (dispatch) => {
	let randomResponse = await fetch(`/api/karuta/random/${cardAmount}`)
	if (randomResponse.ok) {
		const randomResponseJSON = await randomResponse.json();
		const randomResponseNormalized = karutaCardNormalizer(randomResponseJSON.cards);

		// shuffle
		let randomCardsArr = shuffleObj(randomResponseNormalized)
		// console.log("randomCardsArr THUNK: ", randomCardsArr)
		dispatch(loadRandomShuffle(randomCardsArr))
	}
}

// GET and shuffle cards, memory game - OUTPUT: ARRAY
export const getMemoryShuffleRandomKarutaCardsTHUNK = (cardAmount) => async (dispatch) => {
	let randomResponse = await fetch(`/api/karuta/random/${cardAmount}`)
	if (randomResponse.ok) {
		const randomResponseJSON = await randomResponse.json();
		const randomResponseNormalized = karutaCardNormalizer(randomResponseJSON.cards);

		let randomCardsDouble = {};

		Object.values(randomResponseNormalized).map((card) => {
			randomCardsDouble[card.id] = { ...card, 'match': true };
			randomCardsDouble[card.id + 100] = { ...card, 'match': false };
		})

		// shuffle
		let randomCardsArr = shuffleObj(randomCardsDouble)
		// console.log("randomCardsArr THUNK: ", randomCardsArr)

		dispatch(loadRandomShuffle(randomCardsArr))
	}
}

const initialState = {};

export default function karutaReducer(state = initialState, action) {
	switch (action.type) {
		case LOAD_KARUTA_CARDS: {
			const newState = { ...action.payload }
			return newState
		}
		case LOAD_KARUTA_ONE: {
			const newState = { singleCard: action.payload }
			return newState
		}
		case LOAD_RANDOM_SHUFFLE: {
			const newState = { random: action.payload }
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
