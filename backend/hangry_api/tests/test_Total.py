from api.controllers import Delivery, Total
from django_mock_queries.query import MockSet, MockModel


def test_TotalWithDefaultDelivery():
  # Arrange a $15 order that qualifies for the default delivery fee.
  order = MockSet(MockModel(quantity=3, item=MockModel(price=5.0)))
  deliveryFee = Delivery.calculate(order, 2)
  # Act using the real delivery result, as the total endpoint does.
  total = Total.calculate(order, deliveryFee)
  # Assert the $3.50 delivery fee and 8.25% tax are included and rounded.
  assert total == 20.03
