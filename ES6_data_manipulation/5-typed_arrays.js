export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position > length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const arr = new Int8Array(buffer);
  const view = new DataView(buffer);
  arr[position] = value;
  return view;
}
