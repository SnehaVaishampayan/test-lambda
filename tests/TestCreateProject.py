import unittest

import service.CreateProject
from tests.test_constants import error_msg_invalid_pName, fake_project_details_invalid_name, fake_project_details_valid


class Testing(unittest.TestCase):

    def test_validate_project_details(self):
        self.assertTrue(service.CreateProject.validate_project_details(fake_project_details_valid))

    def test_validate_project_details_validate_name(self):
        expected = error_msg_invalid_pName
        with self.assertRaises(Exception) as e:
            service.CreateProject.validate_project_details(fake_project_details_invalid_name)
        self.assertEqual(expected, str(e.exception))


if __name__ == '__main__':
    unittest.main()
