from api.controllers import Tax
from django_mock_queries.query import MockSet, MockModel

def test_SimpleTax():
  #Arrange
  subtotal = 15
  # Tax includes the updated default delivery fee.
  deliveryFee = 3.50
  #Act
  tax = Tax.calculate(subtotal, deliveryFee)
  #Assert
  assert tax == 1.53
