import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTest(unittest.TestCase):

    def setUp(self):
        self.hardware = Hardware("H", "Heavy", 100, 100)

    def test_hardware_init_attributes__expect_correct_values(self):
        self.assertEqual("H", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(100, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_props__expect_correct_result(self):
        self.assertEqual(0, self.hardware.used_memory)
        self.assertEqual(0, self.hardware.used_capacity)

    def test_hardware_install__if_not_enough_space_and_capacity__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hardware.install(Software("S", "Light", 120, 50))
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_uninstall__expect_to_remove_software(self):
        software = Software("S", "Light", 50, 50)
        self.hardware.install(software)
        self.hardware.uninstall(software)
        self.assertNotIn(software, self.hardware.software_components)

if __name__ == "__main__":
    unittest.main()