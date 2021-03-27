import unittest
from project.student import Student


class StudentTests(unittest.TestCase):

    def setUp(self):
        self.student = Student("Hans", None)

    def test_student_init__if_courses_None__expect_initialization(self):
        self.assertEqual("Hans", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init__if_courses_not_None__expect_initialization(self):
        courses = {"Basics": [], "Fundamentals": []}
        self.student = Student("Hans", courses)
        self.assertEqual("Hans", self.student.name)
        self.assertEqual(courses, self.student.courses)

    def test_student_enroll__if_course_not_found_and_notes_to_add__expect_to_add_course_and_notes(self):
        expected_msg = "Course and course notes have been added."
        actual_msg = self.student.enroll("Fundamentals", ["note1, note2"])
        self.assertEqual(expected_msg, actual_msg)
        self.assertEqual(["note1, note2"], self.student.courses["Fundamentals"])

    def test_student_enroll__if_course_not_found__expect_to_add_course(self):
        expected_msg = "Course has been added."
        actual_msg = self.student.enroll("Advanced", [], "add empty list")
        self.assertEqual(expected_msg, actual_msg)
        self.assertEqual([], self.student.courses["Advanced"])

    def test_student_enroll__if_course_found__expect_to_add_notes(self):
        self.student.courses["OOP"] = []
        expected_msg = "Course already added. Notes have been updated."
        actual_msg = self.student.enroll("OOP", ["note1", "note2"])
        self.assertEqual(expected_msg, actual_msg)
        self.assertEqual(["note1", "note2"], self.student.courses["OOP"])

    def test_student_add_notes__if_course_not_found__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Basics", ["note1", "note2"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_student_add_notes__if_course_found__expect_to_add_notes(self):
        self.student.courses["OOP"] = []
        expected_msg = "Notes have been updated"
        actual_msg = self.student.add_notes("OOP", "note1")
        self.assertEqual(expected_msg, actual_msg)
        self.assertEqual(["note1"], self.student.courses["OOP"])

    def test_student_leave_course__if_course_not_found__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Algorithms")

    def test_student_leave_course__if_course_found__expect_course_to_be_removed(self):
        self.student.courses["OOP"] = []
        expected_msg = "Course has been removed"
        actual_msg = self.student.leave_course("OOP")
        self.assertEqual(expected_msg, actual_msg)

if __name__ == "__main__":
    unittest.main()