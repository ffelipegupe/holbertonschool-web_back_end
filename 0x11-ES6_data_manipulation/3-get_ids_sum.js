export default function getStudentIdsSum(students) {
    if (Object.getPrototypeOf(students) === Array.prototype) {
      const ids = students.map((items) => items.id);
      const reducer = (accumulator, currentValue) => accumulator + currentValue;
      return ids.reduce(reducer);
    }
    return [];
  }