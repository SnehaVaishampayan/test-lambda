import unittest
import importlib

CreateProject = importlib.import_module("gsp-create-project")

from tests.test_Constants import error_msg_invalid_pName, fake_project_details_invalid_name, fake_project_details_valid


class Testing(unittest.TestCase):

    def test_validate_project_details(self):
        self.assertTrue(CreateProject.validate_project_details(fake_project_details_valid))

    def test_validate_project_details_validate_name(self):
        expected = error_msg_invalid_pName
        with self.assertRaises(Exception) as e:
            CreateProject.validate_project_details(fake_project_details_invalid_name)
        self.assertEqual(expected, str(e.exception))


if __name__ == '__main__':
    unittest.main()
