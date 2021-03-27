import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle(50, 100)

    def test_vehicle_init__expect_initialization(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_vehicle_drive__if_not_enough_fuel__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_vehicle_drive__if_enough_fuel__execute(self):
        self.vehicle.drive(20)
        self.assertEqual(25, self.vehicle.fuel)

    def test_vehicle_refuel__if_over_capacity__expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(25)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_vehicle_refuel__if_within_capacity__execute(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(10)
        self.assertEqual(35, self.vehicle.fuel)

    def test_vehicle_str__to_return_str_message(self):
        expected_msg = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual_msg = self.vehicle.__str__()
        self.assertEqual(expected_msg, actual_msg)

    def test_vehicle_cls_attr__expect_correct_values(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)


if __name__ == "__main__":
    unittest.main()