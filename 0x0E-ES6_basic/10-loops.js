export default function appendToEachArrayValue(array, appendString) {
    const tempArray = array;
    for (const element of array) {
      const idx = array.indexOf(element);
      tempArray[idx] = `${appendString}${element}`;
    }
  
    return tempArray;
  }