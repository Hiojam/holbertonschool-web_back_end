export default function cleanSet(aSet, startString) {
  if (startString === '' || !startString) return '';
  if (typeof startString !== 'string') return '';
  const filterValues = Array.from(aSet)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.substring(startString.length));
  return filterValues.join('-');
}
