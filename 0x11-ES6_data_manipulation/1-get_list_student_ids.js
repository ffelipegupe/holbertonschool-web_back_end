export default function getListStudentIds(students) {
    // Array checking
    if (Array.isArray(students)) {
      return students.map((items) => items.id);
    }
    return [];
  }