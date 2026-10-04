from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel
import pytest

def test_LotsOfItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  order.add(MockModel(quantity=5))
  delivery_distance = 6
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 7.5

def test_MiddleOfTheRoadItems():
  #Arrange
  order = MockSet()
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  order.add(MockModel(quantity=2))
  delivery_distance = 4
  #Act
  cost = Delivery.calculate(order,delivery_distance)
  #Assert
  assert cost == 5

@pytest.mark.parametrize("quantities, del_dist", [
  ((3, 1), 2),
  ((5,), 4),
  ((6,), 3),
  ((10,), 3),
  ((11,), 3),
  ((15,), 0),
  ((1,), 10),
])
def test_LittleItems(quantities, del_dist):
  #Arrange
  # Cover small orders and tier boundaries that still use the default fee.
  order = MockSet()
  for quantity in quantities:
    order.add(MockModel(quantity=quantity))
  #Act
  cost = Delivery.calculate(order, del_dist)
  #Assert
  assert cost == 3.50
