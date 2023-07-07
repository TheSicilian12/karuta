// Accepts an array, returns an object with keys equal to the items id
export const normalizer = (data) => {
  let newObj = {}
  data.forEach(item => {
    newObj[item.id] = item
  })
  return newObj
}

//Specifically for formatting the karuta card data
// Accepts an array, returns an object with keys equal to the items id AND formats the data to match the karuta data requirements
export const karutaCardNormalizer = (data) => {
  let newObj = {}
  data.forEach(item => {
    newObj[item.id] = {
      'author': {
        'english': '',
        'japanese': '',
        'romaji': ''
      },
      'english': {
        0: '',
        1: '',
        2: '',
        3: '',
        4: ''
      },
      'japanese': {
        0: '',
        1: '',
        2: '',
        3: '',
        4: ''
      },
      'romaji': {
        0: '',
        1: '',
        2: '',
        3: '',
        4: ''
      }
    }
  })
}
