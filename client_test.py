import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], (quote['top_bid']['price']), (quote['top_ask']['price']), ((quote['top_bid']['price']) + float(quote['top_ask']['price']))/2 ))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], (quote['top_bid']['price']), (quote['top_ask']['price']), ((quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2))

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    prices = [
      {'price1': 121.2, 'price2': 132.2},
      {'price1': 65.8, 'price2': 33.2},
    ]
    """ ------------ Add the assertion below ------------ """
    for price in prices:
      self.assertEqual(getRatio(price['price1'], price['price2']), (price['price1'])/price['price2'])

  def test_getRatio_calculateRatioDivByZero(self):
    prices = [
      {'price1': 121.2, 'price2': 0},
      {'price1': 65.8, 'price2': 0},
    ]
    """ ------------ Add the assertion below ------------ """
    for price in prices:
      self.assertIsNone(getRatio(price['price1'], price['price2']))

  def test_getRatio_calculateRatioZeroNumerator(self):
    prices = [
      {'price1': 0, 'price2': 132.2},
      {'price1': 0, 'price2': 33.2},
    ]
    """ ------------ Add the assertion below ------------ """
    for price in prices:
      self.assertEqual(getRatio(price['price1'], price['price2']), 0)

if __name__ == '__main__':
    unittest.main()
