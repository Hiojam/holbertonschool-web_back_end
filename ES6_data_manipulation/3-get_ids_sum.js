export default function getStudentIdsSum(listStudents) {
  const idsStudents = listStudents.map((idFinder) => idFinder.id);
  const idsSummed = idsStudents.reduce((acum, actualNumber) => acum + actualNumber, 0);
  return idsSummed;
}
