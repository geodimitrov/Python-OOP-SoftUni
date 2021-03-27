import unittest
from car_manager import Car

class CarManagerTests(unittest.TestCase):

    def setUp(self):
        self.car = Car("Ford", "Mondeo", 10, 50)

    # test refuel method
    def test_car_refuel__if_amount_to_add_less_than_0__expect_exception(self):
        amount_to_add = -4
        with self.assertRaises(Exception):
            self.car.refuel(amount_to_add)

    def test_car_refuel__if_amount_to_add_above_0_and_total_amount_within_capacity__expect_correct_result(self):
        amount_to_add = 10
        self.car.refuel(amount_to_add)
        self.assertEqual(10, self.car.fuel_amount)

    def test_car_refuel__if_amount_to_add_above_0_and_total_amount_greater_than_capacity__expect_correct_result(self):
        amount_to_add = 56
        self.car.refuel(amount_to_add)
        self.assertEqual(50, self.car.fuel_amount)

    #test drive method
    def test_car_drive__if_needed_fuel_greater_than_total_fuel__expect_exception(self):
        distance = 600
        self.car.refuel(30)
        with self.assertRaises(Exception):
            self.car.drive(distance)

    def test_car_drive__if_needed_fuel_less_or_equal_to_total_fuel__expect_correct_result(self):
        distance = 150
        self.car.refuel(30)
        self.car.drive(distance)
        self.assertEqual(15, self.car.fuel_amount)

    # test the properties
    def test_car_make_property__if_empty_string_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.make = ""

    def test_car_model_property__if_empty_string_expect_exception(self):
        with self.assertRaises(Exception):
            self.car.model = ""

    def test_car_fuel_consumption__if_negative_number_or_0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -8

    def test_car_fuel_capacity__if_negative_number_or_0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

if __name__ == "__main__":
    unittest.main()