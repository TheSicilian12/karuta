export const shuffleObj = (obj) => {
  // input: an obj with id keys
  // output: an array with the index values randomly placed

  let entryObj = Object.values(obj);
  if (entryObj.length === 0) return "undefined";

  let randomArr = [];

  while(entryObj.length > 0) {
    let randomNum = Math.floor(Math.random() * entryObj.length)

    let randomCard = entryObj[randomNum];
    randomArr.push(randomCard);
    entryObj.splice(randomNum, 1);
  }

  return randomArr
}
