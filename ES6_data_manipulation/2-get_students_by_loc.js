export default function getStudentsByLocation(listStudents, cityString) {
  return listStudents.filter((obj) => obj.location === cityString);
}
