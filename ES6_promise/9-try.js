export default function guardrail(mathFunction) {
  const queue = [];

  try {
    queue.push(mathFunction(), 'Guardrail was processed');
  } catch (err) {
    queue.push(err.toString(), 'Guardrail was processed');
  }

  return queue;
}
