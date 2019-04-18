
import unittest

from custom_functions import temperature_methods

class TestLaboratory(unittest.TestCase):

    def test_calculate_prom(self):
        departament_list = [24, 23, 21, 24, 25, 24, 22, 30, 25, 27, 29, 22]
        promedio = temperature_methods.calculate_prom(departament_list)

        self.assertEqual(promedio, 24.666666666666668)

    def test_hottest_temperature(self):
        departament_list = [24, 23, 21, 24, 25, 24, 22, 30, 25, 27, 29, 22]
        hot_temperature = temperature_methods.hottest_temperature(departament_list)

        self.assertEqual(hot_temperature, 30)

    def test_pos_element(self):
        departament_list = [24, 23, 21, 24, 25, 24, 22, 30, 25, 27, 29, 22]
        pos_element = temperature_methods.pos_item(departament_list)

        self.assertEqual(pos_element, 8)



if __name__ == '__main__':
    unittest.main()
