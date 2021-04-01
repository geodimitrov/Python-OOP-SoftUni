import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class HardwareTest(unittest.TestCase):

    def setUp(self):
        self.hardware = Hardware("H", "Power", 100, 80)

    def test_hardware_init__expect_correct_result_upon_initialization(self):
        self.assertEqual("H", self.hardware.name)
        self.assertEqual("Power", self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(80, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_init__expect_int_values(self):
        self.assertEqual(type(100), type(self.hardware.capacity))
        self.assertEqual(type(80), type(self.hardware.memory))

    def test_hardware_install__if_not_enough_capacity__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hardware.install(Software("S", "Light", 120, 50))
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_hardware_install__if_not_enough_memory__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hardware.install(Software("S", "Light", 80, 100))
        self.assertEqual("Software cannot be installed", str(ex.exception))

    # def test_hardware_install__if_enough_capacity_and_memory__expect_correct_result(self):
    #     self.hardware.install(Software("S", "Light", 80, 50))
    #     self.assertEqual(1, len(self.hardware.software_components))

    def test_hardware_uninstall__expect_to_remove_software(self):
        self.hardware.install(Software("S", "Light", 80, 50))
        self.hardware.uninstall(Software("S", "Light", 80, 50))
        self.assertEqual(0, len(self.hardware.software_components))

if __name__ == "__main__":
    unittest.main()