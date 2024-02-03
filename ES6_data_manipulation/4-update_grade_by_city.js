export default function updateStudentGradeByCity(listStudents, cityString, newGrades) {
  const studentsCity = listStudents
    .filter((student) => student.location === cityString)
    .map((data) => {
      const matchingGradeId = newGrades.find((grade) => grade.studentId === data.id);
      const grade = matchingGradeId ? matchingGradeId.grade : 'N/A';
      return { ...data, grade };
    });
  return studentsCity;
}
