import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            data_point = getDataPoint(quote)
            self.assertIsInstance(data_point, tuple)
            self.assertEqual(len(data_point), 4)
            self.assertIsInstance(data_point[0], str)
            self.assertIsInstance(data_point[1], float)
            self.assertIsInstance(data_point[2], float)
            self.assertIsInstance(data_point[3], float)

    def test_getRatio_withNonZeroPrices(self):
        price_a = 120.0
        price_b = 110.0
        ratio = getRatio(price_a, price_b)
        self.assertIsInstance(ratio, float)
        self.assertEqual(ratio, price_a / price_b)

    def test_getRatio_withZeroPriceB(self):
        price_a = 120.0
        price_b = 0.0
        ratio = getRatio(price_a, price_b)
        self.assertIsNone(ratio)

    def test_getRatio_withZeroPriceA(self):
        price_a = 0.0
        price_b = 110.0
        ratio = getRatio(price_a, price_b)
        self.assertEqual(ratio, 0.0)

if __name__ == '__main__':
    unittest.main()
