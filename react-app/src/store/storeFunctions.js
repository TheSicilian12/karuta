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
      'id': item.id,
      'author': {
        'english': item.english_author,
        'japanese': item.japanese_author,
        'romaji': item.romaji_author
      },
      'english': {
        0: item.english_line1,
        1: item.english_line2,
        2: item.english_line3,
        3: item.english_line4,
        4: item.english_line5
      },
      'japanese': {
        0: item.japanese_line1,
        1: item.japanese_line2,
        2: item.japanese_line3,
        3: item.japanese_line4,
        4: item.japanese_line5
      },
      'romaji': {
        0: item.romaji_line1,
        1: item.romaji_line2,
        2: item.romaji_line3,
        3: item.romaji_line4,
        4: item.romaji_line5
      }
    }
  })
  return newObj
}
