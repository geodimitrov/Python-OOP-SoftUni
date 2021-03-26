import unittest
from worker import Worker

class WorkerTests(unittest.TestCase):
    name = "Gosho"
    salary = 1000
    energy = 5

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    """Test if the Worker is initialized with correct name, salary and energy"""
    def test_worker_init__if_correct_info__expect_initialization(self):
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)


    """Test if the Worker's energy is incremented after the rest method is called"""
    def test_worker_rest__expect_energy_to_be_incremented(self):
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    """Test if an error is raised if the Worker tries to work with negative energy or equal to 0"""
    def test_worker_work__when_energy_is_0__expect_exception(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    """Test if the Worker's money is increased by his salary correctly after the work method is called"""
    def test_worker_work__when_energy_is_above_zero__expect_money_to_be_increased(self):
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    """Test if the Worker's energy is decreased after the work method is called"""
    def test_worker_work__when_energy_is_above_zero__expect_energy_to_be_decreased(self):
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    """Test if the get_info method returns the proper string with correct values"""
    def test_worker_get_info__expect_correct_values(self):
        expected_msg = f'{self.name} has saved 0 money.'
        actual_msg = self.worker.get_info()
        self.assertEqual(expected_msg, actual_msg)

if __name__ == "__main__":
    unittest.main()