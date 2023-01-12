import unittest
from main import Teacher
from main import Student
from main import teachers_list
from main import student_list


#to start the test use following command: python3 -m unittest -v test.py


class TestTeacherMethods(unittest.TestCase):
    def setUp(self):
        self.teacher = Teacher("John Smith", "01/01/1970", "123456")
        self.teacher.add_teacher("John Smith", "01/01/1970", "123456")

    def test_add_teacher(self):
        self.assertEqual(len(teachers_list), 1)
        self.assertEqual(teachers_list[0].name, "John Smith")
        self.assertEqual(teachers_list[0].birthdate, "01/01/1970")
        self.assertEqual(teachers_list[0].id, "123456")

    def test_display_teacher(self):
        self.assertEqual(self.teacher.display_teacher(teachers_list[0]),
                         "Name: John Smith\nBirthdate: 01/01/1970\nId: 123456")

    def test_search_teacher(self):
        self.assertEqual(self.teacher.search_teacher(
            "123456"), teachers_list[0])
        self.assertIsNone(self.teacher.search_teacher("not_exists"))

    def test_delete_teacher(self):
        self.teacher.delete_teacher("123456")
        self.assertEqual(len(teachers_list), 0)

    def test_update_teacher(self):
        self.teacher.update_teacher("123456", "Jane Doe", "01/01/1980")
        self.assertEqual(teachers_list[0].name, "Jane Doe")
        self.assertEqual(teachers_list[0].birthdate, "01/01/1980")

    def test_update_non_existent_teacher(self):
        self.assertIsNone(self.teacher.update_teacher(
            "not_exists", "Jane Doe", "01/01/1980"))


class TestStudentMethods(unittest.TestCase):
    def setUp(self):
        self.student = Student("John Smith", "01/01/1970", "123456")
        self.student.add_student("John Smith", "01/01/1970", "123456")

    def test_add_student(self):
        self.assertEqual(len(student_list), 1)
        self.assertEqual(student_list[0].name, "John Smith")
        self.assertEqual(student_list[0].birthdate, "01/01/1970")
        self.assertEqual(student_list[0].id, "123456")

    def test_display_student(self):
        self.assertEqual(self.student.display_student(student_list[0]),
                         "Name: John Smith\nBirthdate: 01/01/1970\nId: 123456")

    def test_search_student(self):
        self.assertEqual(self.student.search_student(
            "123456"), student_list[0])
        self.assertIsNone(self.student.search_student("not_exists"))

    def test_delete_student(self):
        self.student.delete_student("123456")
        self.assertEqual(len(student_list), 0)

    def test_update_student(self):
        self.student.update_student("123456", "Jane Doe", "01/01/1980")
        self.assertEqual(student_list[0].name, "Jane Doe")
        self.assertEqual(student_list[0].birthdate, "01/01/1980")

    def test_update_non_existent_student(self):
        self.assertIsNone(self.student.update_student(
            "not_exists", "Jane Doe", "01/01/1980"))

if __name__ == '__main__':
    unittest.main()
