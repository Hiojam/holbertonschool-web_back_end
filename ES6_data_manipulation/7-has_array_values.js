export default function hasValuesFromArray(aSet, anArray) {
  for (const element of anArray) {
    if (aSet.has(element) === false) {
      return false;
    }
  }
  return true;
}
